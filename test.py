import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databaseTESTBOT import add_user, check_user_register, all_info
from config import TOKEN



logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

def line_button():
    inline_list = [
        [InlineKeyboardButton(text="test", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test2", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test3", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="CLICK HERE", callback_data="Variant1")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_list)

def second_button():
    keyboard = [
        [InlineKeyboardButton(text="Button A", callback_data="A")],
        [InlineKeyboardButton(text="Button B", callback_data="B")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Hi")

@dp.message(Command("register"))
async def register_user(message: types.Message):
    
    telegram_id = message.from_user.id
    user_data = check_user_register(telegram_id)
    name = message.from_user.first_name
    if user_data is None:
        add_user(telegram_id, name)
        await message.answer("You are successfully registered!")
    else:
        await message.answer(f"""Welcome  
{user_data[0]}\n
{user_data[1]}\n
{user_data[2]}

""")
       




#Кнопки инлайн (под сообщением)
@dp.message(Command("123"))
async def get_button(message: types.Message):
    await message.answer("123", reply_markup=line_button())

#Изменяем кнопки (под сообщением)
@dp.callback_query(lambda c: c.data == "Variant1")
async def get_new_variable(callback: CallbackQuery):
    await callback.message.edit_text(
        "You chose Option 1",
        reply_markup= second_button()
    )



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот работает")
    asyncio.run(main())