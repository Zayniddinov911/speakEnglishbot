import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
wikipedia.set_lang('en')
API_TOKEN = '5765266596:AAEUcs6KxXbfYYf4CaicI0B65wB2pAom_18'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("It all starts with the command 'start!' ")


@dp.message_handler()
async def fromWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('There is not match for this request!!!')


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)