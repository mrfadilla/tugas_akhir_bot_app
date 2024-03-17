from telethon import TelegramClient, events

#import library untuk konfigurasi
from dotenv import dotenv_values

from src import process

env = dotenv_values(".env")
bot = TelegramClient("test", env['API_ID'], env['API_HASH']).start(bot_token=env['BOT_TOKEN'])

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    '''send message when the command /start is issued.'''
    await event.reply('Halo, selamat datang di Kuliner Bandung, untuk bertanya seputar kuliner silahkan diawali dengan #tanyadong')

@bot.on(events.NewMessage(pattern='#tanyadong'))
async def tanya_dong(event):
    '''answering the question from dataset.'''

    data = event.text.split()
    data.pop(0)
    data = ' '.join(data)
    result = process.search_services(data, env)

    await event.respond(f"{result}")

def run():
    '''start the bot'''
    print("aplikasi berjalan")
    bot.run_until_disconnected()
