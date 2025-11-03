import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

level = {}

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"we are in")

@bot.event
async def on_message(message, level, member):
    if message.author == bot.user:
        return
    
    if ":3" in message.content:
        await message.reply(":headr0cking_it:")
        level[{member}] += 1
    await bot.process_commands(message)
    return level



bot.run(token, level, log_handler=handler, log_level=logging.DEBUG)