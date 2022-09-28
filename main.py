import logging
from aiogram import Bot, Dispatcher, executor, types
from oxforddict import getDefinitions
from googletrans import Translator
API_TOKEN = '5765266596:AAEUcs6KxXbfYYf4CaicI0B65wB2pAom_18'

translator = Translator()
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("It all starts with the command 'start!' ")


@dp.message_handler(commands=['help'])
async def ask_help(message: types.Message):
    await message.answer('What can I help you, my friend!')

@dp.message_handler()
async def interpreter(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'ru' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

