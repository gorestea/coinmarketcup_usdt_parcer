import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import Token
from main import check_update

bot = Bot(token=Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

paused = False

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Старт автоматизации", "Стоп автоматизации"]
    keyboad = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboad.add(*start_buttons)
    hello = "Здравствуйте!\n" \
        "Этот бот разработан под Авито. Пожалуйста, настройте все критерии на сайте.\n" \
        "Для работы введите команду <b>/url</b> и укажите рядом ссылку.\n" \
        "Чтобы получить все товары по ссылке в формате Excel - нажмите на кнопку <b>'Все товары(файл)</b>'\n" \
        "Кнопка <b>'Старт автоматизации'</b> позволяет запустить автоматическое обновление товаров по ссылке, новые товары отправляются ботом в сообщении\n" \
        "Кнопка <b>'Стоп автоматизации'</b> останавливает автоматизацию. Чтобы запустить автоматизацию снова - нажмите 'Старт автоматизации'\n" \
        "Кнопка <b>'Непросмотренные товары'</b> позволяет получить те товары, которые были упущены во время остановки автоматизации с помощью кнопки 'Стоп автоматизации'\n" \
        "Если возникнут какие-то вопросы, затруднения - пишите мне в телеграмм или на почту: <u>rojofamily@yandex.ru</u>"
    await message.answer(hello, reply_markup=keyboad)

@dp.message_handler(Text(equals="Стоп автоматизации"))
async def stop(message: types.Message):
    global paused
    paused = True
    await message.answer("Бот остановлен")
    return paused

@dp.message_handler(Text(equals="Старт автоматизации"))
async def message_every_minute(message: types.Message):
    await message.answer("Автоматизация начата")
    global paused
    paused = False
    while paused == False:
                fresh = check_update()
                if fresh == None:
                    await asyncio.sleep(15)
                    continue
                await message.answer(fresh)
                await asyncio.sleep(15)
    return paused

if __name__ == '__main__':
    executor.start_polling(dp)
