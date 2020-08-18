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