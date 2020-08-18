from bot import bot, dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from config import admin_id

from keybords.default import menu
from datetime import datetime

from SQLighter import SQLighter
sqlite = SQLighter('user_database.sqlite')


@dp.message_handler(Command('start'))
async def show_menu(message: Message):
    await message.answer('Здравствуйте ! \nЭто бот для контролирования ваших расходов', reply_markup=menu)


@dp.message_handler(Command('add'))
async def add_recording(message: Message):
    user_msg = message.text.split()[1:]
    if user_msg:
        sqlite.insert_to(*user_msg)
        text = 'Запись добавлена !'
        await bot.send_message(chat_id=message.chat.id, text=text)
    else:
        text = 'Введите название записи !'
        await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands=['select_today'])
async def select_today(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='За сегодня :')
    expenses = sqlite.select_today()
    await message.answer(text=expenses)


@dp.message_handler(commands=['select_week'])
async def select_week(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='За неделю :')
    expenses = sqlite.select_week()
    await message.answer(text=expenses)


@dp.message_handler(commands=['select_month'])
async def select_month(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='За месяц :')
    expenses = sqlite.select_month()
    await message.answer(text=expenses)