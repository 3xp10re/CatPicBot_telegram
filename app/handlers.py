from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import random

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("для отправки котика жмякните 'котик!'", reply_markup=kb.main)

@router.message(F.text == 'памагите!!!(((')
async def help(message: Message):
    await message.answer("жмякните 'котик!'", reply_markup=kb.main)

@router.message(F.text == 'котик!')
async def cat(message: Message):
    with open ('cat_urls.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()
    await message.answer_photo(random.choice(links))