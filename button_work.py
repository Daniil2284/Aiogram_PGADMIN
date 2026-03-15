from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery

def line_button_test():
    inline_list = [
        [InlineKeyboardButton(text="test", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test2", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="test3", url='https://habr.com/ru/articles/820877/')],
        [InlineKeyboardButton(text="CLICK HERE", callback_data="Variant1")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_list)

def line_desc_button_work():
    keyboard = [
        [InlineKeyboardButton(text="🧹 Уборщик", callback_data="work_desc_level_1")],
        [InlineKeyboardButton(text="📦 Грузчик", callback_data="work_desc_level_2")],
        [InlineKeyboardButton(text="🚕 Таксист", callback_data="work_desc_level_3")],
        [InlineKeyboardButton(text="🚚 Дальнобойщик", callback_data="work_desc_level_4")],
        [InlineKeyboardButton(text="🚄 Водитель электропоезда", callback_data="work_desc_level_5")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def line_button_work(callback_data1):
    
    keyboard = [
        [InlineKeyboardButton(text="🔶 Начать работу", callback_data=callback_data1)],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
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