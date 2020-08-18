from aiogram import Bot, Dispatcher, executor

from config import BOT_TOKEN, admin_id, config_id

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handler import *
    executor.start_polling(dp, skip_updates=True)



# self.bot.get_updates
# return await self.message_handlers.notify(update.message)