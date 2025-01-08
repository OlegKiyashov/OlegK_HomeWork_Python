from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Строка подключения к БД
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем подключение и сессию
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def get_session():
    # Функция возвращает новую сессию для работы с БД.
    return Session()
