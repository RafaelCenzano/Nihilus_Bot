
import discord
from discord.ext import commands
import asyncio
import random
import json
import os

bot = commands.Bot(command_prefix='.', description='testing')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.group(pass_context=True)
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@bot.command(aliases=["commands"])
async def command():
    await bot.say('```md\n# Command List #\n```\n**Use prefix . when doing commands**\n**[Command Category]** Then list of commands in the categories\n**1. Core -** `messages`\n**2. Dice - ** `d4` `d6` `d8` `d10` `d12` `d20`\n**3. Misc - ** `wake` `sleep`')

file_path = os.path.join('/Users/savagecoder/Desktop/Programming/pass.json')
with open(file_path, 'r') as token_data:
    data = json.load(token_data)
    discord_token = (data['discord_token'])
bot.run(discord_token)
