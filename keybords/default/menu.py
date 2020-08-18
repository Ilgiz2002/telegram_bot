from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
      keyboard=[
            [
                  KeyboardButton(text='Мои расходы')
            ],
            [
                  KeyboardButton(text='Добавить запись'),
            ],
      ],
      resize_keyboard=True
)

menu_date = ReplyKeyboardMarkup(
      keyboard=[
            [
                  KeyboardButton(text='За сегодня')
            ],
            [
                  KeyboardButton(text='За неделю'),
            ],
            [
                  KeyboardButton(text='За месяц'),
            ],
            [
                  KeyboardButton(text='Назад на главное меню'),
            ],
      ],
      resize_keyboard=True
)