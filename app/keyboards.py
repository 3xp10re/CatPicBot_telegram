from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='котик!')],
                                     [KeyboardButton(text='памагите!!!(((')]], resize_keyboard=True,
                           input_field_placeholder='выберите опцию...')
