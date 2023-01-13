from telethon import TelegramClient, events
import os
from dotenv import load_dotenv
load_dotenv()

# Use your own API ID and HASH (https://my.telegram.org/)
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')


client = TelegramClient('session_name', api_id, api_hash)

client.start(bot_token=bot_token)
print("Bot Started !")


@client.on(events.NewMessage)
async def handle_commands(event):
    # Check if the message starts with '/news'
    if event.message.message.startswith('/news'):
        # Split the message by space to separate the command and argument
        cmd, arg = event.message.message.split(' ', 1)
        if arg:
            await event.reply("market news " + arg)
        else:
            await event.reply("market news")

client.run_until_disconnected()
