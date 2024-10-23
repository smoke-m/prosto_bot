"""Модуль операций CRUD."""

from sqlalchemy import select

from .db import RequestsInfo, UsersInfo, AsyncSessionLocal


class CRUDBase:
    """Базовые операции CRUD."""

    def __init__(self, model):
        self.model = model

    async def create(
            self,
            data_dict: dict,
    ):
        """запись в базу объекта класса."""
        obj = self.model(**data_dict)
        async with AsyncSessionLocal() as session:
            session.add(obj)
            await session.commit()

    async def get_by_attribute(
            self,
            attr_name: str,
            attr_value: str,
    ):
        """получение объекта по атрибуту."""
        attr = getattr(self.model, attr_name)
        async with AsyncSessionLocal() as session:
            db_obj = await session.execute(
                select(self.model).where(attr == attr_value)
            )
        return db_obj.scalars().all()

    async def remove(
            self,
            db_obj,
    ):
        """Удаление объекта."""
        async with AsyncSessionLocal() as session:
            await session.delete(db_obj)
            await session.commit()


class CRUDRequestsInfo(CRUDBase):
    """Операции CRUD для модели RequestsInfo."""

    async def get_last(
            self,
            user_nic: str,
    ):
        """Получение последнего запроса к боту."""
        async with AsyncSessionLocal() as session:
            db_obj = await session.execute(
                select(self.model)
                .where(self.model.user_nic == user_nic)
                .order_by(self.model.id.desc())
            )
        return db_obj.scalars().first()


class CRUDUsersInfo(CRUDBase):
    """Операции CRUD для модели UsersInfo."""

    async def get_multi(
            self,
    ):
        """Получение всех пользователей."""
        async with AsyncSessionLocal() as session:
            db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()


requests_info_crud = CRUDRequestsInfo(RequestsInfo)
users_info_crud = CRUDUsersInfo(UsersInfo)
