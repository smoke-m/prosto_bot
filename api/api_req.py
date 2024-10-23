import aiohttp

from aiogram_bot.constants import URL_API_USD


async def task():
    async with aiohttp.ClientSession() as session:
        response = await session.get(URL_API_USD)
        data = await response.json(content_type=None)
    return data['Valute']['USD']['Value']
