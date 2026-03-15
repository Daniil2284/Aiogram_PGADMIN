import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN


from handler.work_handler import work_handler_main
from handler.profile import profile_user
from handler.register import register_user

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

dp = Dispatcher()

register_user(dp)
profile_user(dp)
work_handler_main(dp)

# connector = ProxyConnector.from_url("socks5://127.0.0.1:10808")
# session = AiohttpSession(connector=connector)

# # session = AiohttpSession(api=TelegramAPIServer.from_base("http://localhost:8081", is_local=True))
# bot = Bot(token=TOKEN,session=session)
# dp = Dispatcher()

# def line_button():
#     inline_list = [
#         [InlineKeyboardButton(text="test", url='https://habr.com/ru/articles/820877/')],
#         [InlineKeyboardButton(text="test2", url='https://habr.com/ru/articles/820877/')],
#         [InlineKeyboardButton(text="test3", url='https://habr.com/ru/articles/820877/')],
#         [InlineKeyboardButton(text="CLICK HERE", callback_data="Variant1")]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=inline_list)

# def second_button():
#     keyboard = [
#         [InlineKeyboardButton(text="Button A", callback_data="A")],
#         [InlineKeyboardButton(text="Button B", callback_data="B")]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=keyboard)



# @dp.message(Command("work"))
# async def working(message: types.Message):
#     button_work.line_button_work()

#     telegram_id = message.from_user.id
#     user_data = check_user_register(telegram_id)
#     balance = int(user_data[2]) + 100
#     update_balance(balance, telegram_id)
#     await message.answer(f"Your balance {balance}")



#Кнопки инлайн (под сообщением)
# @dp.message(Command("123"))
# async def get_button(message: types.Message):
#     await message.answer("123", reply_markup=line_button())

# #Изменяем кнопки (под сообщением)
# @dp.callback_query(lambda c: c.data == "Variant1")
# async def get_new_variable(callback: CallbackQuery):
#     await callback.message.edit_text(
#         "You chose Option 1",
#         reply_markup= second_button()
#     )


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот работает")
    asyncio.run(main())