from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery

def line_button_test():
    inline_list = [
        [InlineKeyboardButton(text="test", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test2", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test3", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="CLICK HERE", callback_data="Variant1")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_list)

def line_button_work():
    keyboard = [
        [InlineKeyboardButton(text="Работа 1", callback_data="work_level_1")],
        [InlineKeyboardButton(text="Работа 2", callback_data="work_level_2")],
        [InlineKeyboardButton(text="Работа 3", callback_data="work_level_3")],
        [InlineKeyboardButton(text="Работа 4", callback_data="work_level_4")],
        [InlineKeyboardButton(text="Работа 5", callback_data="work_level_5")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def line_button_profile():
    pass

def line_button_shop_car():
    pass

def line_button_casino():
    pass

def line_button_bank():
    pass

def line_button_inventory():
    pass