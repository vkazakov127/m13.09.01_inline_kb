# -*- coding: utf-8 -*-
# m13.09.01_inline_kb.py
# Кнопка 'Информация', не отрабатывает завершение вызова
# ---------------------------------------------------------
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = "ABCDEF"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button1)


@dp.message_handler(commands=['start', 'Start', 'START'])
async def starter(message):
    await message.answer("Рады вас видеть!", reply_markup=kb)


@dp.callback_query_handler(text='info')
async def infor(call):
    await call.message.answer('Информация о боте')  #
    await call.answer()   # Тут вызов должен завершиться, но он не завершается


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
