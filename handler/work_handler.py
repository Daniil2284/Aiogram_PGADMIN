import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databaseTESTBOT import add_user, check_user_register, update_balance
import button_work
from handler.salary_work import salary
from handler.salary_work import delay_work



def work_handler_main(dp):

    
    @dp.message(Command("work"))
    async def working(message: types.Message):
        telegram_id = message.from_user.id
        user_data = check_user_register(telegram_id)
        if not user_data:
            await message.answer("❌ Сначала зарегистрируйся через /start")
            return

        await message.answer("WORK", reply_markup= button_work.line_button_work())

    @dp.callback_query(lambda c: c.data == "work_level_1")
    async def get_cash(callback: CallbackQuery):
        telegram_id = callback.from_user.id
        user_data = check_user_register(telegram_id)
        
        allowed = await delay_work(telegram_id, callback)
        if not allowed:
            return

        balance = int(user_data[2]) + salary[0]
        update_balance(balance, telegram_id)
        await callback.answer()
        await callback.message.edit_text(f"Your balance {balance}")
