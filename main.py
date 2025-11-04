import discord
from discord.ext import commands
import os

token = os.getenv('replyRockBotToken')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"we are in")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if ":3" in message.content:
        await message.reply("<:headr0cking_it:1399193497407586455>")
    
    await bot.process_commands(message)

bot.run(token)
