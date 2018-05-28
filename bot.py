
import discord
from discord.ext import commands
import asyncio
import random
import json
import os
import math

bot = commands.Bot(command_prefix='.', description='testing')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.group(pass_context=True)
async def punch(ctx, chosen_user: discord.Member):
    punch_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    if chosen_user2 == punch_author:
        await bot.say(':fist: You uhhhh want to do what {}??'.format(punch_author))
        await bot.send_file(ctx.message.channel, 'Images_and_Gifs/selfpunch.gif')
    else:
        await bot.say(':fist: {} punched {}'.format(punch_author, chosen_user2))
        random_gif = random.randint(1,12)
        if random_gif <= 3:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/punch1.gif')
        elif 4 <= random_gif <= 6:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/punch2.gif')
        elif 7 <= random_gif <= 9:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/punch3.gif')
        else:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/punch4.gif')

@bot.group(pass_context=True, aliases=["high5"])
async def highfive(ctx, chosen_user: discord.Member):
    highfive_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    if chosen_user2 == highfive_author:
        await bot.say(':hand_splayed: You uhhhh want to do what {}??'.format(highfive_author))
        await bot.send_file(ctx.message.channel, 'Images_and_Gifs/selffive.gif')
    else:
        await bot.say(':hand_splayed: {} high fived {}'.format(highfive_author, chosen_user2))
        random_gif = random.randint(1,12)
        if random_gif <= 3:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/highfive1.gif')
        elif 4 <= random_gif <= 6:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/highfive2.gif')
        elif 7 <= random_gif <= 9:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/highfive3.gif')
        else:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/highfive4.gif')

@bot.group(pass_context=True)
async def slap(ctx, chosen_user: discord.Member):
    slap_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    if chosen_user2 == slap_author:
        await bot.say(':raised_back_of_hand: You uhhhh want to do what {}??'.format(slap_author))
        await bot.send_file(ctx.message.channel, 'Images_and_Gifs/slap_yourself.gif')
    else:
        await bot.say(':raised_back_of_hand: {} slapped {}'.format(slap_author, chosen_user2))
        random_gif = random.randint(1,12)
        if random_gif <= 3:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/slap1.gif')
        elif 4 <= random_gif <= 6:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/slap2.gif')
        elif 7 <= random_gif <= 9:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/slap3.gif')
        else:
            await bot.send_file(ctx.message.channel, 'Images_and_Gifs/slap4.gif')

@bot.group(pass_context=True)
async def cool(ctx, chosen_user: discord.Member):
    cool_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    cool_message = await bot.say('{} wants to see if {} is cool'.format(cool_author, chosen_user2))
    await asyncio.sleep(1.7)
    cool_or_not_cool = [":cool:", "cool", "cool", "kinda cool", "just OK", "not cool"]
    random_cool_not_cool = '{} is {}'.format(chosen_user2, random.choice(cool_or_not_cool))
    await bot.edit_message(cool_message, random_cool_not_cool)

@bot.command(aliases=["commands"])
async def command():
    await bot.say('```md\n# Command List #\n```\n**Use prefix . when doing commands**\n**[Command Category]** Then list of commands in the categories\nUse .help [command] to find out how to use the command\nDo not include []\n**1. Core -** `highfive` `slap`\n**2. Math - ** `add` `subtract` `multiply` `divide`\n**3. Dice - ** `d4` `d6` `d8` `d10` `d12` `d20`')

@bot.command(aliases=["hi"])
async def hello():
    await bot.say('Hello! :speech_balloon:')

@bot.command()
async def add(first_number : float, second_number : float):
    await bot.say(first_number + second_number)

@bot.command()
async def subtract(first_number : float, second_number : float):
    await bot.say(first_number - second_number)

@bot.command()
async def multiply(first_number : float, second_number : float):
    await bot.say(first_number * second_number)

@bot.command()
async def divide(first_number : float, second_number : float):
    await bot.say(first_number / second_number)

@bot.command(aliases=["sqrt"])
async def squareroot(number : float):
    if number > 0:
        squarerooted_number = math.sqrt(number)
        await bot.say(squarerooted_number)
    else:
        await bot.say('The number is negative or will give a nonreal number')

@bot.command()
async def d4():
    roll_message = await bot.say('rolling ...')
    d4_roll = ["1", "2", "3", "4"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d4_roll))

@bot.command()
async def d6(aliases=["dice"]):
    roll_message = await bot.say('rolling ...')
    d6_roll = ["1", "2", "3", "4", "5", "6"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d6_roll))

@bot.command()
async def d8():
    roll_message = await bot.say('rolling ...')
    d8_roll = ["1", "2", "3", "4", "5", "6", "7", "8"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d8_roll))

@bot.command()
async def d10():
    roll_message = await bot.say('rolling ...')
    d10_roll = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d10_roll))

@bot.command()
async def d12():
    roll_message = await bot.say('rolling ...')
    d12_roll = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d12_roll))

@bot.command()
async def d20():
    roll_message = await bot.say('rolling ...')
    d20_roll = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "**20!!, Critical Hit**"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d20_roll))

@bot.command(pass_context=True, aliases=["money", "currency"])
async def credits(ctx):
    credits_author = str(ctx.message.author)
    credits_author_mention = ctx.message.author.mention
    player_data_path = os.path.join('/Users/savagecoder/Desktop/Programming/Enchanter77_Discord_Bot/Json_files/User_data.json')
    with open(player_data_path, 'r') as profile_data:
        profile_data1 = json.load(profile_data)
    if credits_author in profile_data1['userdata']:
        user_credits = profile_data1['userdata'][credits_author]['credits']
        await bot.say(f':credit_card: {credits_author_mention} has {user_credits} credits!')
    else:
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][credits_author] = {"daily":0, "credits":0, "level":1, "xp":0, "streak":0, "rep":0}
            json.dump(profile_data1, outfile)
        await bot.say(f':credit_card: {credits_author_mention} has 0 credits!')

@bot.command(pass_context=True)
async def daily(ctx):
    daily_author = str(ctx.message.author)
    daily_author_mention = ctx.message.author.mention
    player_data_path = os.path.join('/Users/savagecoder/Desktop/Programming/Enchanter77_Discord_Bot/Json_files/User_data.json')
    with open(player_data_path, 'r') as profile_data:
        daily_data1 = json.load(profile_data)
    if daily_author in daily_data1['userdata']:
        if daily_data1['userdata'][daily_author]['daily'] != 1:
            if daily_data1['userdata'][daily_author]['level'] <= 25:
                await bot.say(f'{daily_author_mention} got 150 credits for their daily')
                with open(player_data_path, 'w') as outfile:
                    daily_data1['userdata'][daily_author]['credits'] += 150
                    daily_data1['userdata'][daily_author]['daily'] += 1
                    daily_data1['userdata'][daily_author]['xp'] += 5
                    json.dump(daily_data1, outfile)
                with open(player_data_path, 'r') as level_data:
                    daily_data_level_check = json.load(level_data)
                if daily_data_level_check['userdata'][daily_author]['xp'] >= 200:
                    with open(player_data_path, 'w') as outfile:
                        daily_data1['userdata'][daily_author]['level'] += 1
                        daily_data1['userdata'][daily_author]['xp'] = 0
                        json.dump(daily_data1, outfile)
                    with open(player_data_path, 'r') as level_data:
                        daily_data_level = json.load(level_data)
                    daily_new_level = daily_data_level['userdata'][daily_author]['level']
                    await bot.say(f'{daily_author_mention} has leveled up to {daily_new_level}')
            else:
                await bot.say(f'{daily_author_mention} got 200 credits for their daily')
                with open(player_data_path, 'w') as outfile:
                    daily_data1['userdata'][daily_author]['credits'] += 150
                    daily_data1['userdata'][daily_author]['daily'] += 1
                    daily_data1['userdata'][daily_author]['xp'] += 5
                    json.dump(daily_data1, outfile)
        else:
            await bot.say('You redeemed your daily already')
        #user_daily = profile_data1['userdata'][credits_author]['daily']
        #await bot.say(f':credit_card: {daily_author_mention} has {user_credits} credits!')
    else:
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][credits_author] = {"daily":1, "credits":150, "level":1, "xp":5, "streak":0, "rep":0}
            json.dump(profile_data1, outfile)
        await bot.say(f'{daily_author_mention} got 150 credits for their daily')

file_path = os.path.join('/Users/savagecoder/Desktop/Programming/pass.json')
with open(file_path, 'r') as token_data:
    data = json.load(token_data)
    discord_token = data['discord_token']
bot.run(discord_token)
