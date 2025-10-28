import g4f
import telebot
import logging
from typing import Dict, Any

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Конфигурация (в продакшене используйте переменные окружения)
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Замените на ваш токен

bot = telebot.TeleBot(BOT_TOKEN)
user_data: Dict[int, Dict[str, Any]] = {}


class BotStates:
    WAITING_FIRST_TEAM = 1
    WAITING_SECOND_TEAM = 2
    WAITING_H2H = 3
    WAITING_HOME_TEAM = 4
    WAITING_SCORES = 5
    WAITING_FIRST_SERIES = 6
    WAITING_SECOND_SERIES = 7


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    bot.send_message(
        user_id,
        "Привет! Я бот для анализа футбольных матчей. "
        "Давайте проанализируем предстоящую игру!"
    )
    ask_first_team(user_id)


def ask_first_team(user_id):
    bot.send_message(user_id, "🔵 Укажите первую команду:")
    bot.register_next_step_handler_by_chat_id(user_id, process_first_team)


def process_first_team(message):
    try:
        user_id = message.from_user.id
        first_team = message.text.strip()

        if not first_team:
            bot.send_message(user_id, "❌ Название команды не может быть пустым. Попробуйте снова:")
            bot.register_next_step_handler_by_chat_id(user_id, process_first_team)
            return

        user_data[user_id]["first_team"] = first_team
        ask_second_team(user_id)

    except Exception as e:
        logger.error(f"Error in process_first_team: {e}")
        bot.send_message(user_id, "❌ Произошла ошибка. Давайте начнем заново. Используйте /start")


def ask_second_team(user_id):
    bot.send_message(user_id, "🔴 Укажите вторую команду:")
    bot.register_next_step_handler_by_chat_id(user_id, process_second_team)


def process_second_team(message):
    try:
        user_id = message.from_user.id
        second_team = message.text.strip()

        if not second_team:
            bot.send_message(user_id, "❌ Название команды не может быть пустым. Попробуйте снова:")
            bot.register_next_step_handler_by_chat_id(user_id, process_second_team)
            return

        user_data[user_id]["second_team"] = second_team
        ask_h2h_info(user_id)

    except Exception as e:
        logger.error(f"Error in process_second_team: {e}")
        bot.send_message(user_id, "❌ Произошла ошибка. Давайте начнем заново. Используйте /start")


def ask_h2h_info(user_id):
    first_team = user_data[user_id]["first_team"]
    second_team = user_data[user_id]["second_team"]

    bot.send_message(
        user_id,
        f"📊 Укажите статистику личных встреч {first_team} и {second_team} за последние 5 лет:\n"
        f"Формат: Победы_первой-Ничьи-Поражения_первой\n"
        f"Пример: 3-2-1"
    )
    bot.register_next_step_handler_by_chat_id(user_id, process_h2h_info)


def process_h2h_info(message):
    try:
        user_id = message.from_user.id
        h2h_info = message.text.strip()

        # Простая валидация формата
        if '-' not in h2h_info or len(h2h_info.split('-')) != 3:
            bot.send_message(user_id, "❌ Неверный формат. Используйте формат: Число-Число-Число\nПопробуйте снова:")
            bot.register_next_step_handler_by_chat_id(user_id, process_h2h_info)
            return

        user_data[user_id]["h2h_info"] = h2h_info
        ask_home_team(user_id)

    except Exception as e:
        logger.error(f"Error in process_h2h_info: {e}")
        bot.send_message(user_id, "❌ Произошла ошибка. Давайте начнем заново. Используйте /start")


def ask_home_team(user_id):
    first_team = user_data[user_id]["first_team"]
    second_team = user_data[user_id]["second_team"]

    bot.send_message(
        user_id,
        f"🏠 Какая команда играет дома?\n"
        f"Варианты:\n"
        f"• {first_team}\n"
        f"• {second_team}\n"
        f"• нет"
    )
    bot.register_next_step_handler_by_chat_id(user_id, process_home_team)


def process_home_team(message):
    try:
        user_id = message.from_user.id
        home_team = message.text.strip().lower()

        valid_answers = [
            user_data[user_id]["first_team"].lower(),
            user_data[user_id]["second_team"].lower(),
            'нет'
        ]

        if home_team not in valid_answers:
            bot.send_message(user_id, "❌ Пожалуйста, укажите одну из предложенных команд или 'нет':")
            bot.register_next_step_handler_by_chat_id(user_id, process_home_team)
            return

        user_data[user_id]["home_team"] = message.text
        ask_scores(user_id)

    except Exception as e:
        logger.error(f"Error in process_home_team: {e}")
        bot.send_message(user_id, "❌ Произошла ошибка. Давайте начнем заново. Используйте /start")


def ask_scores(user_id):
    bot.send_message(
        user_id,
        "⚽ Какой счет был в последних двух матчах каждой команды?\n"
        "Формат: счет_команды1, счет_команды2\n"
        "Пример: 2-1 0-0, 3-2 1-1"
    )
    bot.register_next_step_handler_by_chat_id(user_id, process_scores)


def process_scores(message):
    try:
        user_id = message.from_user.id
        user_data[user_id]["scores"] = message.text
        ask_series(user_id)

    except Exception as e:
        logger.error(f"Error in process_scores: {e}")
        bot.send_message(user_id, "❌ Произошла ошибка. Давайте начнем заново. Используйте /start")


def ask_series(user_id):
    first_team = user_data[user_id]["first_team"]
    bot.send_message(user_id, f"📈 Какая серия побед у {first_team}? (например: 3 победы подряд)")
    bot.register_next_step_handler_by_chat_id(user_id, lambda msg: process_series(msg, "first_team"))


def process_series(message, team_key):
    try:
        user_id = message.from_user.id

        if "series" not in user_data[user_id]:
            user_data[user_id]["series"] = {}

        user_data[user_id]["series"][team_key] = message.text

        if team_key == "first_team":
            second_team = user_data[user_id]["second_team"]
            bot.send_message(user_id, f"📈 Какая серия побед у {second_team}?")
            bot.register_next_step_handler_by_chat_id(user_id, lambda msg: process_series(msg, "second_team"))
        else:
            calculate_win_chance(user_id)

    except Exception as e:
        logger.error(f"Error in process_series: {e}")
        bot.send_message(user_id, "❌ Произошла ошибка. Давайте начнем заново. Используйте /start")


def assemble_query(user_id):
    data = user_data[user_id]

    query = f"""
Проанализируй футбольный матч между командами:
- Команда 1: {data['first_team']}
- Команда 2: {data['second_team']}

Статистика личных встреч за 5 лет (Победы-Ничьи-Поражения): {data['h2h_info']}
Домашняя команда: {data['home_team']}
Результаты последних матчей: {data['scores']}
Серия побед {data['first_team']}: {data['series']['first_team']}
Серия побед {data['second_team']}: {data['series']['second_team']}

Рассчитай вероятности в процентах:
1. Победа {data['first_team']}
2. Победа {data['second_team']} 
3. Ничья

Учти все факторы: личные встречи, домашнее поле, текущая форма, серии.
Ответ предоставь на русском языке в виде анализа и итоговых вероятностей.
"""
    return query


def calculate_win_chance(user_id):
    try:
        bot.send_message(user_id, "🔄 Анализирую данные и рассчитываю вероятности...")
        query = assemble_query(user_id)
        process_user_input(query, user_id)

    except Exception as e:
        logger.error(f"Error in calculate_win_chance: {e}")
        bot.send_message(user_id, "❌ Ошибка при анализе данных. Попробуйте снова /start")


def process_user_input(input_text, user_id):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input_text}],
            stream=False,
        )

        if response:
            # Ограничиваем длину сообщения для Telegram
            message_text = str(response)[:4000]
            bot.send_message(user_id, message_text, parse_mode='Markdown')
        else:
            bot.send_message(user_id, "❌ Не удалось получить анализ. Попробуйте позже.")

    except Exception as e:
        logger.error(f"Error in process_user_input: {e}")
        bot.send_message(user_id, "❌ Ошибка при обращении к AI. Попробуйте позже.")


@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """
🤖 Футбольный аналитик бот

Команды:
/start - начать анализ матча
/help - показать эту справку
/id - показать ваш ID

Как использовать:
1. Запустите /start
2. Введите названия команд
3. Укажите статистику личных встреч
4. Ответьте на вопросы о матче
5. Получите анализ вероятностей

Форматы данных:
- Статистика H2H: 3-2-1 (победы-ничьи-поражения)
- Счет: 2-1 0-0, 3-2 1-1
    """
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['id'])
def show_id(message):
    bot.send_message(message.chat.id, f"🆔 Ваш ID: `{message.from_user.id}`", parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Используйте /start для анализа матча или /help для справки")


if __name__ == "__main__":
    logger.info("Бот запущен...")
    bot.polling(none_stop=True)