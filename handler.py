from bot import bot, dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from config import admin_id

from keybords.default import menu
from datetime import datetime

from SQLighter import SQLighter
sqlite = SQLighter('user_database.sqlite')


# @dp.message_handler(Command('menu'))
# async def show_menu(message: Message):
#     await message.answer("Выберите товар из меню ниже", reply_markup=menu)

# @dp.message_handler(Text(equals=["Котлетки", "Макарошки", "Пюрешка"]))
# async def show_console(message: Message):
#     await message.answer(text=f'Вы заказали : {message.text}')


    

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


@dp.message_handler(commands=['del'])
async def delete_recording(message: Message):
    user_msg = message.text.split()[1:]
    sqlite.delete_from(' '.join(user_msg))


# @dp.message_handler(commands=['select_today'])
# async def select_today(message: Message):
#     res = sqlite.select_today()
#     await message.answer('За сегодня :')
#     price = []
#     for line in res:
#         await bot.send_message(chat_id=message.chat.id, text=f'{line[0]}\n {line[1]} - {line[2]} сум')
#         price.append(line[2])
#     await message.answer(f'Потрачено : {sum(price)} сум')

def get_expenses(res):
    expenses = {}
    for line in res:
        if line[0] not in expenses.keys():
            expenses[line[0]] = [[line[1], line[2]]]
        else:
            expenses[line[0]] += [[line[1], line[2]]]
    return expenses


@dp.message_handler(commands=['select_today'])
async def select_today(message: Message):
    res = sqlite.select_today()
    await message.answer('За сегодня :')
    
    expenses = get_expenses(res)

    await message.answer(text=expenses)
    await message.answer(f'Потрачено : {sum(price)} сум')


    
@dp.message_handler(commands=['select_week'])
async def select_week(message: Message):
    res = sqlite.select_week()
    await message.answer('За неделю :')

    expenses = get_expenses(res)
    print(str(expenses))
    string = ''
    for date in expenses.keys():
        string + str(date)
        # for item in expenses[date]:
        #     string + f'\n\t{item[0]} - {item[1]}'
    print('This is string', string)
    # await message.answer(text=string)
    # await message.answer(f'Потрачено : {sum(price)} сум')
    # price = []
    # for line in res:
    #     await bot.send_message(chat_id=message.chat.id, text=f'{line[0]}\n {line[1]} - {line[2]} сум')
    #     price.append(line[2])
    # await message.answer(f'Потрачено : {sum(price)} сум')


@dp.message_handler(commands=['select_month'])
async def select_month(message: Message):
    res = sqlite.select_month()
    await message.answer('За месяц :')
    price = []
    for line in res:
        await bot.send_message(chat_id=message.chat.id, text=f'{line[0]}\n {line[1]} - {line[2]} сум')
        price.append(line[2])
    await message.answer(f'Потрачено : {sum(price)} сум')