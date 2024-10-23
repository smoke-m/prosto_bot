from .crud import users_info_crud


async def user_in_db(
        user_nic: str,
):
    """Есть ли юзер в базе."""
    if await users_info_crud.get_by_attribute('user_nic', user_nic):
        return True
    else:
        return False
