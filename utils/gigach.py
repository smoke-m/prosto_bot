import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat

from aiogram_bot.constants import SYSTEM_MSG

load_dotenv()


def get_ansver(msg):
    llm = GigaChat(
        credentials=os.getenv("CREDENTIALS"),
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs=False,
        streaming=False,
    )

    messages = [SystemMessage(content=SYSTEM_MSG)]
    messages.append(HumanMessage(content=msg))
    res = llm.invoke(messages)
    messages.append(res)
    return res.content
