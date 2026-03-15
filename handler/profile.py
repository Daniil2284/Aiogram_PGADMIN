import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databaseTESTBOT import add_user, check_user_register, update_balance


def profile_user(dp):
    @dp.message(Command("profile"))
    async def send_welcome(message: types.Message):
        telegram_id = message.from_user.id
        try:

            user_data = check_user_register(telegram_id)
            exp = user_data[14] or 0
            max_exp = user_data[15] or 1000
            percent_blocks = int((exp / max_exp) * 10)
            percent_real = (exp / max_exp) * 100
            progress_bar = "🟩" * percent_blocks  + "⬜" * (10 - percent_blocks )
            profile_text = f"""

    📊 <b>Твой профиль:</b>

    🆔 ID: {user_data[0]}
    👤 Имя: {user_data[1]}
    📛 Username: {"@" + user_data[3] if user_data[3] else "нет"}

    💷 Баланс: {user_data[2]} ₽
    💶 Bitcoin: {user_data[4] } ₿ 
    👑 Золото: {user_data[5] } кг
    🪙 Монет: {user_data[6] } BC

    🏠 Дом: {user_data[7] } 
    🚗 Машины: {user_data[8]}
    💼 Бизнес: {user_data[9]}

    🏦 Банк: {user_data[10] } ₽
    📈 Депозит: {user_data[11] } ₽

    🎮 Уровень: {user_data[13]}
    📈 Опыт: {exp}/{max_exp} ({percent_real:.1f}%)
    {progress_bar})
    📅 Регистрация: {user_data[16] if len(user_data) > 16 else 'Неизвестно'}
                    """



            if not user_data:
                await message.answer("❌ Сначала зарегистрируйся через /start")
                return
            else:
                await message.answer(profile_text, parse_mode="HTML")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            await message.answer("❌ [ОШИБКА] Не удалось загрузить профиль")
