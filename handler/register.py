import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databaseTESTBOT import add_user, check_user_register, update_balance



def register_user(dp):
    @dp.message(Command("start"))
    async def register_user(message: types.Message):
        
        telegram_id = message.from_user.id
        
        name = message.from_user.first_name
        username = message.from_user.username
        try:
            user_data = check_user_register(telegram_id)
            if user_data is None:
                add_user(telegram_id, name, username)
                welcome_text = f"""
🎉 Привет, {name}!

Ты успешно зарегистрирован в игре!

💰 Стартовый баланс: 1000 ₽
🎮 Уровень: 1

Используй /profile чтобы посмотреть свой профиль.
                """
                await message.answer(welcome_text, parse_mode="HTML")
            else:
                await message.answer(f"""Welcome  
        {user_data[0]}\n
        {user_data[1]}\n
        {user_data[2]}

        """)
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            await message.answer("❌ Ошибка при регистрации. Попробуй позже.")

