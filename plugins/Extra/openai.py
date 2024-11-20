# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @Tamilbots
# Ask Doubt on telegram @TamilSupport

from pyrogram import Client, filters
from plugins.Extra.engine import ask_ai


@Client.on_message(filters.command('Tamilini'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
