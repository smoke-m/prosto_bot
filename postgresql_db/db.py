"""Модуль создания БД."""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from aiogram_bot.config_bot import config


class PreBase:
    """Базовый класс."""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(config.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session


class RequestsInfo(Base):
    """Модель объекта вопроса от юзера."""

    user_nic = Column(Text,)
    user_request = Column(Text,)


class UsersInfo(Base):
    """Модель информации юзера."""

    user_nic = Column(Text, unique=True,)
