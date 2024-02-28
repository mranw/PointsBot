from aiogram.utils.keyboard import InlineKeyboardBuilder

users_points = 0

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6986359528:AAFA2X2O9aLCej9phgS8yvQhYPQ3CpmpRJs")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /about
@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Узнать мои баллы",
        callback_data="user_points_value")
    )
    await message.answer(
        '''Вы находитесь в боте, который помогает узнать количество накопленных баллов в Школе Насти Рыбки. Чтобы узнать текущую сумму ваших баллов, нажмите кнопку ниже👇''',
        reply_markup = builder.as_markup()
    )


@dp.callback_query(F.data == "user_points_value")
async def send_user_points_value(callback: types.CallbackQuery):
    await callback.message.answer(str(users_points))
    await callback.answer()


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
