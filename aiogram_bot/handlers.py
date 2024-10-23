import logging

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from .keyboards import keyboard_main
from .constants import (
    BUTTON_1, BUTTON_2, BUTTON_3, MISS_MSG, QUESTION_MSG, START_MSG, USERS_MSG
)
from postgresql_db.crud import requests_info_crud, users_info_crud
from postgresql_db.validators import user_in_db
from api.api_req import task
from utils.gigach import get_ansver

logger = logging.getLogger(__name__)
router = Router()


class QuestionState(StatesGroup):
    """Класс состояния."""

    get_question = State()


@router.message(F.text, Command("start"))
async def start_handler(msg: Message):
    """Хендлер старта работы с пользователем."""
    logger.info(f"Получено сообщение {msg.text}")
    await msg.answer(
        START_MSG.format(msg.from_user.full_name),
        reply_markup=keyboard_main
    )


@router.message(F.text.lower() == BUTTON_1.lower())
async def handler_giga_chat(msg: Message, state: FSMContext):
    """Хендлер запуска состояния запроса/ответа к GigaChat."""
    logger.info(f"Получено сообщение {msg.text}")
    await msg.answer(QUESTION_MSG)
    await state.set_state(QuestionState.get_question)


@router.message(QuestionState.get_question)
async def return_info(msg: Message, state: FSMContext):
    """Хендлер запроса/ответа к GigaChat."""
    logger.info(f"Получено сообщение {msg.text}")
    if await user_in_db(msg.from_user.full_name) is False:
        await users_info_crud.create(
            dict(user_nic=msg.from_user.full_name)
        )
    await requests_info_crud.create(dict(
        user_nic=msg.from_user.full_name,
        user_request=msg.text
    ))
    ansver = get_ansver(msg.text)
    await msg.answer(ansver)
    await state.clear()


@router.message(F.text.lower() == BUTTON_2.lower())
async def handler_get_last(msg: Message,):
    """Хендлер получение последнего запроса к боту."""
    logger.info(f"Получено сообщение {msg.text}")
    db_obj = await requests_info_crud.get_last(msg.from_user.full_name)
    await msg.answer(db_obj.user_request)


@router.message(F.text.lower() == BUTTON_3.lower())
async def handler_get_users(msg: Message,):
    """Хендлер получение всех пользователей."""
    msg_answ = USERS_MSG
    logger.info(f"Получено сообщение {msg.text}")
    db_objs = await users_info_crud.get_multi()
    for obj in db_objs:
        msg_answ += (f"{obj.user_nic}\n")
    await msg.answer(msg_answ)


@router.message(F.text.lower() == "dell_secret")
async def handler_del_users(msg: Message,):
    """Хендлер получение всех пользователей и их удаления."""
    logger.info(f"Получено сообщение {msg.text}")
    db_objs = await users_info_crud.get_multi()
    for obj in db_objs:
        await users_info_crud.remove(obj)
    await msg.answer("пользователи удалены")


@router.message()
async def curse(msg: Message):
    """Хендлер для любой фразы."""
    logger.info(f"Получено сообщение {msg.text}")
    await msg.answer(
        MISS_MSG.format(msg.from_user.full_name, await task())
        )
