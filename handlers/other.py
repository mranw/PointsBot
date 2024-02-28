from aiogram import Router, F, html
from aiogram.types import Message


router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Привет! Я бот, который помогает узнать количество накопленных баллов в Школе Насти Рыбки. "
                         "Чтобы узнать свои баллы, нажмите команду /start")


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("К сожалению, я не могу обработать это. Если у вас есть еще вопросы, пожалуйста, задайте их!")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Прошу прощения за путаницу. Чтобы узнать свои баллы в Школе Насти Рыбки, нажмите на команду "
                         "/start")
