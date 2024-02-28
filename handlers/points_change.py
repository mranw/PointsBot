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
    for user in message.text:
        if '+1 балл' in message.text:
            await message.reply(f"Пользователю @{user.full_name} начислен +1 балл")

    if '+2 балла' in message.text:
        await message.reply(f"Пользователю начислено +2 балла")
    elif '+3 балла' in message.text:
        await message.answer(f"Пользователю {message.reply} начислено +3 балла")
    elif '+4 балла' in message.text:
        await message.answer("Пользователю начислено +4 балла")
    elif '+5 балла' in message.text:
        await message.answer("Пользователю начислено +5 баллов")
