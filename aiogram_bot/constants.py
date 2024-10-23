"""Модуль констант проекта."""

# Глобальные настройки логгера
BACKUP_COUNT = 5
ENCODING = "UTF-8"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
LOGGING_LEVEL = "INFO"
LOGS_FOLDER = "logs"
LOGS_FILE = "logfile.log"
MAX_BYTES = 50_000_000

# Константы бота

# Сообщения бота
IN_FILD_PL = "Чем могу помочь?"
START_MSG = (
    "Добрый день {}!\n"
    "Я бот который использует технологию GigaChat.\n"
    "Выбери чем могу помочь?"
)
QUESTION_MSG = "Введите текс вопроса к GigaChat"
USERS_MSG = "Список пользователей: \n"
MISS_MSG = (
    "Дорогой {}, я просто бот!\n"
    "Умею не много.\n"
    "Вот курс доллара к рублю: {}\n"
    "Что бы получить ответ на любой вопрос,\n"
    "Нажми кнопку - Задать вопрос GigaChat,\n"
    "набери вопрос.\n"
)

# Кнопки бота
BUTTON_1 = "Задать вопрос GigaChat"
BUTTON_2 = "О чем я с тобой общался в прошлый раз?"
BUTTON_3 = "Назови мне ники пользователей, которые с тобой общались?"

# RRLs бота
URL_API_USD = "https://www.cbr-xml-daily.ru/daily_json.js"

# Константы GigaChat
SYSTEM_MSG = (
    "Ты эмпатичный бот-психолог, "
    "который помогает пользователю решить его проблемы."
)
