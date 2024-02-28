from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message

router = Router()
users_points = 0


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Узнать мои баллы",
        callback_data="user_points_value")
    )
    await message.answer(
        'Добро пожаловать в бота, который помогает узнать количество накопленных баллов в Школе Насти Рыбки. \nЧтобы '
        'узнать текущую сумму ваших баллов, нажмите кнопку ниже👇',
        reply_markup=builder.as_markup()
    )


@router.message(Command("about"))
async def cmd_about(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Узнать мои баллы",
        callback_data="user_points_value")
    )
    await message.answer(
        'Я бот, который помогает узнать количество накопленных баллов в Школе Насти Рыбки. \nЧтобы '
        'узнать текущую сумму ваших баллов, нажмите кнопку ниже👇',
        reply_markup=builder.as_markup()
    )


@router.message(Command("ban"), F.reply_to_message)
async def cmd_ban(message: Message, admins: set[int]):
    if message.from_user.id not in admins:
        await message.answer(
            "У вас недостаточно прав для совершения этого действия"
        )
    else:
        await message.chat.ban(
            user_id=message.reply_to_message.from_user.id
        )
        await message.answer("Нарушитель заблокирован")


@router.callback_query(F.data == "user_points_value")
async def send_user_points_value(callback: types.CallbackQuery):
    await callback.message.answer(f'Уважаемый {callback.from_user.first_name}, у вас {users_points} баллов.')
    await callback.answer()
