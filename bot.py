#not named bot yet

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

bot.run('TOKEN')