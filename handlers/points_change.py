from typing import List

from aiogram import Router, F
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from filters.find_usernames import HasUsernamesFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(
    F.text,
    HasUsernamesFilter()
)
async def plus_point_message_with_usernames(
        message: Message,
        usernames: List[str]
):
    if '+1 балл' in message.text:
        if len(usernames) == 1:
            await message.reply(f"Пользователю {", ".join(usernames)} начислен +1 балл")
        elif len(usernames) > 1:
            await message.reply(f"Пользователям {", ".join(usernames)} начислен +1 балл")
    elif '+2 балла' in message.text:
        if len(usernames) == 1:
            await message.reply(f"Пользователю {", ".join(usernames)} начислено +2 балла")
        elif len(usernames) > 1:
            await message.reply(f"Пользователям {", ".join(usernames)} начислено +2 балла")
    elif '+3 балла' in message.text:
        if len(usernames) == 1:
            await message.reply(f"Пользователю {", ".join(usernames)} начислено +3 балла")
        elif len(usernames) > 1:
            await message.reply(f"Пользователям {", ".join(usernames)} начислено +3 балла")
    elif '+4 балла' in message.text:
        if len(usernames) == 1:
            await message.reply(f"Пользователю {", ".join(usernames)} начислено +4 балла")
        elif len(usernames) > 1:
            await message.reply(f"Пользователям {", ".join(usernames)} начислено +4 балла")
    elif '+5 баллов' in message.text:
        if len(usernames) == 1:
            await message.reply(f"Пользователю {", ".join(usernames)} начислено +5 баллов")
        elif len(usernames) > 1:
            await message.reply(f"Пользователям {", ".join(usernames)} начислено +5 баллов")
    else:
        if len(usernames) == 1:
            await message.reply("Неверный формат сообщения о начислении баллов.\n\n"
                                f"Пользователю {", ".join(usernames)} не были начислены баллы."
                                "Вы можете начислить до пяти баллов за раз")
        elif len(usernames) > 1:
            await message.reply("Неверный формат сообщения о начислении баллов.\n\n"
                                f"Пользователям {", ".join(usernames)} не были начислены баллы."
                                "Вы можете начислить до пяти баллов за раз")
