from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery

def line_button_work():
    inline_list = [
        [InlineKeyboardButton(text="test", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test2", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test3", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="CLICK HERE", callback_data="Variant1")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_list)