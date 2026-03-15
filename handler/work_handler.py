import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databaseTESTBOT import  check_user_register, update_balance, update_exp, update_level, update_max_exp
import button_work 
from handler.salary_work import salary, add_exp, level_work
from handler.salary_work import delay_work



def work_handler_main(dp):

    
    @dp.message(Command("work"))
    async def working(message: types.Message):
        telegram_id = message.from_user.id
        user_data = check_user_register(telegram_id)
        if not user_data:
            await message.answer("❌ Сначала зарегистрируйся через /start")
            return
        
        desc_work = f"""
        <b>💼 ЗАНЯТОСТЬ</b>
Выбери работу и начни строить свою карьеру 🚀

Работай, зарабатывай деньги 💰, получай опыт ⭐  
и постепенно открывай новые, более прибыльные профессии.

    Каждая работа приносит:
    • 💵 Зарплату  
    • ⭐ Опыт  
    • 📈 Новый уровень возможностей
    
    Случайные события:
    • 💸 Штрафы
    • ⭐ Дополнительные EXP
    • 💎 Редкий предмет (шанс выпадения зависит от работы)

    Каждый шаг приближает тебя к топам проекта 🎯
"""
    
        await message.answer(desc_work, parse_mode="HTML", reply_markup= button_work.line_desc_button_work())



    @dp.callback_query(lambda c: c.data == "work_desc_level_1")
    async def info_work(callback: CallbackQuery):
        desk_work = f"""
╔══════════════╗
        <b>Уборщик:</b>
╚══════════════╝    

💼 <b>Должность:</b> Уборщик улиц
Ты берёшь метлу и выходишь на работу. Город сам себя не уберёт!
Собери мусор, очисти тротуары и получи честно заработанные деньги.

💰 <b>Зарплата:</b> небольшая, но стабильная
⭐ <b>Требуется уровень:</b> 1        
"""
        callback_data1 = "work_level_1"
        await callback.message.edit_text(desk_work, parse_mode="HTML", reply_markup=button_work.line_button_work(callback_data1))





    @dp.callback_query(lambda c: c.data == "work_desc_level_2")
    async def info_work(callback: CallbackQuery):
        desk_work = f"""
╔══════════════╗
        <b>Грузчик:</b>
╚══════════════╝    

💼 <b>Должность:</b> Складской грузчик
Сегодня на складе много коробок. 
Тебе нужно разгрузить фуру и расставить товары по местам.
Работа тяжёлая, но платят уже лучше.

💰 <b>Зарплата:</b> средняя
⭐ <b>Требуется уровень:</b> 3      
"""
        callback_data1 = "work_level_2"
        await callback.message.edit_text(desk_work, parse_mode="HTML", reply_markup=button_work.line_button_work(callback_data1))



    @dp.callback_query(lambda c: c.data == "work_desc_level_3")
    async def info_work(callback: CallbackQuery):
        desk_work = f"""
╔══════════════╗
        <b>Таксист:</b>
╚══════════════╝    

💼 <b>Должность:</b> Водитель такси
Ты берёшь машину и выезжаешь на линию. Пассажиры ждут!
Доставь их быстро и безопасно — возможно получишь хорошие чаевые.

💰 <b>Зарплата:</b> средняя + шанс чаевых
⭐ <b>Требуется уровень:</b> 5      
"""
        callback_data1 = "work_level_3"
        await callback.message.edit_text(desk_work, parse_mode="HTML", reply_markup=button_work.line_button_work(callback_data1))



    @dp.callback_query(lambda c: c.data == "work_desc_level_4")
    async def info_work(callback: CallbackQuery):
        desk_work = f"""
╔══════════════╗
        <b>Дальнобойщик:</b>
╚══════════════╝    

💼 <b>Должность:</b> Водитель дальнобойщика
Ты берёшь грузовик, а после едешь по маршруту. Главное не усни!
Если доставишь груз в целости и сохранности, то есть шанс получить хороший бонус

💰 <b>Зарплата:</b> средняя + шанс доплаты + шанс получить доп EXP
⭐ <b>Требуется уровень:</b> 10      
"""
        callback_data1 = "work_level_4"
        await callback.message.edit_text(desk_work, parse_mode="HTML", reply_markup=button_work.line_button_work(callback_data1))


    @dp.callback_query(lambda c: c.data == "work_desc_level_5")
    async def info_work(callback: CallbackQuery):
        desk_work = f"""
╔══════════════╗
        <b>Водитель электропоезда:</b>
╚══════════════╝    

💼 <b>Должность:</b>  это не просто человек за пультом управления. 
Это высококвалифицированный специалист, прошедший многоэтапное обучение и сертификацию, 
чьи навыки и решения напрямую влияют на безопасность тысяч пассажиров. 

💰 <b>Зарплата:</b> выше средней + шанс выпадения редкого предмета
⭐ <b>Требуется уровень:</b> 15      
"""
        callback_data1 = "work_level_5"
        await callback.message.edit_text(desk_work, parse_mode="HTML", reply_markup=button_work.line_button_work(callback_data1))




    @dp.callback_query(lambda c: c.data == "work_level_1")
    async def get_cash(callback: CallbackQuery):
        
        telegram_id = callback.from_user.id
        user_data = check_user_register(telegram_id)
        
        
        allowed = await delay_work(telegram_id, callback)
        if not allowed:
            return
        # print("BUTTON WORKS")
        balance = int(user_data[2]) + salary[0]
        exp = int(user_data[14]) + add_exp[0]
        max_exp = int(user_data[15])
        level = int(user_data[13])


        while exp >= max_exp:
            exp -= max_exp
            level += 1
            max_exp = int(100 * (level ** 1.5))

        update_balance(balance, telegram_id)
        update_exp(exp, telegram_id)
        update_level(level, telegram_id)
        update_max_exp(max_exp, telegram_id)
        await callback.answer()
        work_message =  f"""
╔══════════════╗
        <b>ИНФОРМАЦИЯ:</b>
╚══════════════╝ 


💰 Ты заработал: {salary[0]} ₽\n
⭐ Твой уровень: {level}\n
📈 Заработал EXP: {add_exp[0]}
"""
        await callback.message.edit_text(work_message, parse_mode="HTML")

    @dp.callback_query(lambda c: c.data == "work_level_2")
    async def get_cash(callback: CallbackQuery):
        
        telegram_id = callback.from_user.id
        user_data = check_user_register(telegram_id)
        level = int(user_data[13])
        required_level = level_work[0]

        if level < required_level:
            await callback.answer(
                f"❌ Недостаточный уровень\n\n"
                f"⭐ Твой уровень: {level}\n"
                f"📈 Нужен: {required_level} уровень",
                show_alert=True
            )
            return

        allowed = await delay_work(telegram_id, callback)
        if not allowed:
            return
        # print("BUTTON WORKS")
        balance = int(user_data[2]) + salary[1]
        exp = int(user_data[14]) + add_exp[1]
        max_exp = int(user_data[15])

        while exp >= max_exp:
            exp -= max_exp
            level += 1
            max_exp = int(100 * (level ** 1.5))
        

        update_balance(balance, telegram_id)
        update_exp(exp, telegram_id)
        update_level(level, telegram_id)
        update_max_exp(max_exp, telegram_id)
        await callback.answer()
        work_message =  f"""
╔══════════════╗
        <b>ИНФОРМАЦИЯ:</b>
╚══════════════╝ 


    💰 Заработал: {salary[0]} ₽\n"
    ⭐ Твой уровень: {level}\n"
    📈 Заработал EXP: {add_exp[0]}"
"""
        await callback.message.edit_text(work_message, parse_mode="HTML")

    @dp.callback_query(lambda c: c.data == "work_level_3")
    async def get_cash(callback: CallbackQuery):
        
        telegram_id = callback.from_user.id
        user_data = check_user_register(telegram_id)
        level = int(user_data[13])
        required_level = level_work[1]

        if level < required_level:
            await callback.answer(
                f"❌ Недостаточный уровень\n\n"
                f"⭐ Твой уровень: {level}\n"
                f"📈 Нужен: {required_level} уровень",
                show_alert=True
            )
            return

        allowed = await delay_work(telegram_id, callback)
        if not allowed:
            return
        # print("BUTTON WORKS")
        balance = int(user_data[2]) + salary[2]
        exp = int(user_data[14]) + add_exp[2]
        max_exp = int(user_data[15])

        while exp >= max_exp:
            exp -= max_exp
            level += 1
            max_exp = int(100 * (level ** 1.5))
        

        update_balance(balance, telegram_id)
        update_exp(exp, telegram_id)
        update_level(level, telegram_id)
        update_max_exp(max_exp, telegram_id)
        await callback.answer()
        work_message =  f"""
╔══════════════╗
        <b>ИНФОРМАЦИЯ:</b>
╚══════════════╝ 


    💰 Заработал: {salary[0]} ₽\n"
    ⭐ Твой уровень: {level}\n"
    📈 Заработал EXP: {add_exp[0]}"
"""
        await callback.message.edit_text(work_message, parse_mode="HTML")

    @dp.callback_query(lambda c: c.data == "work_level_4")
    async def get_cash(callback: CallbackQuery):
        
        telegram_id = callback.from_user.id
        user_data = check_user_register(telegram_id)
        level = int(user_data[13])
        required_level = level_work[2]

        if level < required_level:
            await callback.answer(
                f"❌ Недостаточный уровень\n\n"
                f"⭐ Твой уровень: {level}\n"
                f"📈 Нужен: {required_level} уровень",
                show_alert=True
            )
            return

        allowed = await delay_work(telegram_id, callback)
        if not allowed:
            return
        # print("BUTTON WORKS")
        balance = int(user_data[2]) + salary[3]
        exp = int(user_data[14]) + add_exp[3]
        max_exp = int(user_data[15])

        while exp >= max_exp:
            exp -= max_exp
            level += 1
            max_exp = int(100 * (level ** 1.5))
        

        update_balance(balance, telegram_id)
        update_exp(exp, telegram_id)
        update_level(level, telegram_id)
        update_max_exp(max_exp, telegram_id)
        await callback.answer()
        work_message =  f"""
╔══════════════╗
        <b>ИНФОРМАЦИЯ:</b>
╚══════════════╝ 


    💰 Заработал: {salary[0]} ₽\n"
    ⭐ Твой уровень: {level}\n"
    📈 Заработал EXP: {add_exp[0]}"
"""
        await callback.message.edit_text(work_message, parse_mode="HTML")

    @dp.callback_query(lambda c: c.data == "work_level_5")
    async def get_cash(callback: CallbackQuery):
        
        telegram_id = callback.from_user.id
        user_data = check_user_register(telegram_id)
        level = int(user_data[13])
        required_level = level_work[3]

        if level < required_level:
            await callback.answer(
                f"❌ Недостаточный уровень\n\n"
                f"⭐ Твой уровень: {level}\n"
                f"📈 Нужен: {required_level} уровень",
                show_alert=True
            )
            return

        allowed = await delay_work(telegram_id, callback)
        if not allowed:
            return
        # print("BUTTON WORKS")
        balance = int(user_data[2]) + salary[4]
        exp = int(user_data[14]) + add_exp[4]
        max_exp = int(user_data[15])

        while exp >= max_exp:
            exp -= max_exp
            level += 1
            max_exp = int(100 * (level ** 1.5))
        

        update_balance(balance, telegram_id)
        update_exp(exp, telegram_id)
        update_level(level, telegram_id)
        update_max_exp(max_exp, telegram_id)
        await callback.answer()
        work_message =  f"""
╔══════════════╗
        <b>ИНФОРМАЦИЯ:</b>
╚══════════════╝ 


    💰 Заработал: {salary[0]} ₽\n"
    ⭐ Твой уровень: {level}\n"
    📈 Заработал EXP: {add_exp[0]}"
"""
        await callback.message.edit_text(work_message, parse_mode="HTML")




