🇷🇺 Русская версия
⚽ Футбольный аналитик бот для Telegram
Telegram бот для анализа футбольных матчей с использованием AI. Бот собирает ключевую информацию о предстоящем матче и с помощью нейросети (GPT) предоставляет детальный анализ с расчетом вероятностей исходов.

🚀 Возможности
Сбор ключевых данных: названия команд, статистика личных встреч, домашнее поле, последние результаты, серии побед

AI-анализ: интеллектуальный анализ матча с учетом всех факторов

Расчет вероятностей: оценка шансов на победу каждой команды и ничью

Удобный диалог: пошаговый сбор информации через Telegram

Логирование: полное логирование процессов для отладки

🛠 Технологии
python-telegram-bot - работа с Telegram API

g4f - бесплатное использование GPT моделей

logging - система логирования

typing - типизация для лучшей поддерживаемости кода

📦 Установка и запуск
Клонируйте репозиторий:

bash
git clone https://github.com/yourusername/football-analyst-bot.git
cd football-analyst-bot
Установите зависимости:

bash
pip install -r requirements.txt
Настройте бота:

Создайте бота через @BotFather

Получите токен

Замените YOUR_BOT_TOKEN_HERE в коде на ваш токен

Запустите бота:

bash
python bot.py
📋 Использование
Запустите бота: отправьте команду /start

Введите данные:

Названия двух команд

Статистику личных встреч (формат: 3-2-1)

Информацию о домашней команде

Результаты последних матчей

Серии побед команд

Получите анализ: AI обработает данные и вернет детальный анализ с вероятностями

Доступные команды:
/start - начать анализ матча

/help - показать справку

/id - показать ваш ID в Telegram

⚙️ Конфигурация
Основные настройки в коде:

python
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Токен бота
Для продакшена рекомендуется:

Использовать переменные окружения для токена

Настроить веб-хуки вместо polling

Добавить обработку ошибок и retry логику

🏗 Архитектура
Бот использует конечный автомат для управления диалогом:

WAITING_FIRST_TEAM → WAITING_SECOND_TEAM → WAITING_H2H → ...

Данные пользователей хранятся в памяти в user_data

Каждый шаг валидирует ввод пользователя

🤝 Разработка
Для внесения изменений:

Форкните репозиторий

Создайте ветку для фичи (git checkout -b feature/amazing-feature)

Закоммитьте изменения (git commit -m 'Add amazing feature')

Запушьте ветку (git push origin feature/amazing-feature)

Создайте Pull Request

⚠️ Ограничения
Данные пользователей хранятся в памяти (сбрасываются при перезапуске)

Для продакшена требуется персистентное хранилище

Точность анализа зависит от качества входных данных

📄 Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для деталей.

🇺🇸 English Version
⚽ Football Analyst Telegram Bot
Telegram bot for football match analysis using AI. The bot collects key information about upcoming matches and uses neural networks (GPT) to provide detailed analysis with outcome probability calculations.

🚀 Features
Key data collection: team names, head-to-head statistics, home field advantage, recent results, winning streaks

AI analysis: intelligent match analysis considering all factors

Probability calculation: win/draw probabilities for each team

User-friendly dialog: step-by-step data collection via Telegram

Logging: comprehensive process logging for debugging

🛠 Technologies
python-telegram-bot - Telegram API integration

g4f - free GPT models usage

logging - logging system

typing - typing for better code maintainability

📦 Installation & Setup
Clone the repository:

bash
git clone https://github.com/yourusername/football-analyst-bot.git
cd football-analyst-bot
Install dependencies:

bash
pip install -r requirements.txt
Configure the bot:

Create a bot via @BotFather

Get the token

Replace YOUR_BOT_TOKEN_HERE in the code with your token

Run the bot:

bash
python bot.py
📋 Usage
Start the bot: send /start command

Enter data:

Names of both teams

Head-to-head statistics (format: 3-2-1)

Home team information

Recent match results

Team winning streaks

Get analysis: AI processes data and returns detailed analysis with probabilities

Available commands:
/start - start match analysis

/help - show help

/id - show your Telegram ID

⚙️ Configuration
Main settings in code:

python
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Bot token
For production recommended:

Use environment variables for tokens

Configure webhooks instead of polling

Add error handling and retry logic

🏗 Architecture
The bot uses a state machine for dialog management:

WAITING_FIRST_TEAM → WAITING_SECOND_TEAM → WAITING_H2H → ...

User data stored in memory in user_data

Each step validates user input

🤝 Development
To contribute:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Create a Pull Request

⚠️ Limitations
User data stored in memory (resets on restart)

Persistent storage required for production

Analysis accuracy depends on input data quality

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📁 Рекомендуемая структура репозитория:
text
football-analyst-bot/
├── README.md          # Это описание
├── bot.py            # Основной код бота
├── requirements.txt   # Зависимости
├── .gitignore        # Git ignore файл
└── LICENSE           # Лицензия
📝 requirements.txt:
text
g4f
pytelegrambotapi
