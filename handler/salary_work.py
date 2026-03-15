from datetime import datetime, timedelta
import random 

salary = [random.randint(10,100),random.randint(100,500),random.randint(500,1500),random.randint(1500,3000)]
add_exp = [random.randint(1000,10000),random.randint(100,500),random.randint(100,500),random.randint(100,500),random.randint(100,500)]
level_work = [3, 5, 10, 15, 20]


work_cooldown = {}
async def delay_work(telegram_id, callback: CallbackQuery):
    
    now = datetime.now() 
    if telegram_id in work_cooldown:
        last_time = work_cooldown[telegram_id]

        if now - last_time < timedelta(minutes=5):
            remaining = timedelta(minutes=5) - (now - last_time)
            seconds = int(remaining.total_seconds())

            await callback.answer(
                f"⏳ Подожди {seconds} сек перед следующей работой",
                show_alert=True
            )
            return False
        
    work_cooldown[telegram_id] = now
    return True

