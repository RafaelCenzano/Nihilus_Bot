import discord
from discord.ext import commands
import asyncio
import random
import json
import os
import math

bot = commands.Bot(command_prefix='.', description='Bot with economy and other fun commands')
player_data_path = os.path.join('/Users/savagecoder/Desktop/Programming/Enchanter77_Discord_Bot/Json_files/User_data.json')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Use .commands"))

async def check_level(ctx):
    command_author = str(ctx.message.author)
    command_author_mention = ctx.message.author.mention
    with open(player_data_path, 'r') as profile_data:
        command_data1 = json.load(profile_data)
    if command_author in profile_data1['userdata']:
        if command_data1['userdata'][command_author]['xp'] >= 200:
            with open(player_data_path, 'w') as outfile:
                command_data1['userdata'][command_author]['level'] += 1
                command_data1['userdata'][command_author]['xp'] = 0
                json.dump(command_data1, outfile)
            with open(player_data_path, 'r') as level_data:
                command_data_level = json.load(level_data)
            command_new_level = command_data_level['userdata'][command_author]['level']
            await bot.say(f'{command_author_mention} has leveled up to {command_new_level}')
        else:
            pass
    else:
        pass

async def add_1_xp(ctx):
    command_author = str(ctx.message.author)
    command_author_mention = ctx.message.author.mention
    with open(player_data_path, 'r') as profile_data:
        command_data1 = json.load(profile_data)
    if command_author in command_data1['userdata']:
        with open(player_data_path, 'w') as outfile:
            command_data1['userdata'][command_author]['xp'] += 1
            json.dump(command_data1, outfile)
    else:
        pass

@bot.group(pass_context=True, description='punch any Discord member')
async def punch(ctx, chosen_user: discord.Member):
    punch_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    if chosen_user2 == punch_author:
        await bot.say(':fist: You uhhhh want to do what {}??'.format(punch_author))
        await bot.send_file(ctx.message.channel, 'Images_and_Gifs/selfpunch.gif')
        await add_1_xp(ctx)
        await check_level(ctx)
    else:
        await add_1_xp(ctx)
        await check_level(ctx)
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

@bot.group(pass_context=True, aliases=["high5"], description='highfive any Discord member')
async def highfive(ctx, chosen_user: discord.Member):
    highfive_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    if chosen_user2 == highfive_author:
        await bot.say(':hand_splayed: You uhhhh want to do what {}??'.format(highfive_author))
        await bot.send_file(ctx.message.channel, 'Images_and_Gifs/selffive.gif')
        await add_1_xp(ctx)
        await check_level(ctx)
    else:
        await add_1_xp(ctx)
        await check_level(ctx)
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

@bot.group(pass_context=True, description='slap any Discord member')
async def slap(ctx, chosen_user: discord.Member):
    slap_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    if chosen_user2 == slap_author:
        await bot.say(':raised_back_of_hand: You uhhhh want to do what {}??'.format(slap_author))
        await bot.send_file(ctx.message.channel, 'Images_and_Gifs/slap_yourself.gif')
        await add_1_xp(ctx)
        await check_level(ctx)
    else:
        await add_1_xp(ctx)
        await check_level(ctx)
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

@bot.command(pass_context=True, description='rep another player to give them reputation points')
async def rep(ctx, chosen_user: discord.Member):
    rep_author = str(ctx.message.author)
    rep_author_mention = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    chosen_user_rep = str(chosen_user)
    with open(player_data_path, 'r') as profile_data:
        profile_data1 = json.load(profile_data)
    if rep_author in profile_data1['userdata']:
        check_if_repped = profile_data1['userdata'][rep_author]['repped']
        if check_if_repped == 0:
            if chosen_user_rep in profile_data1['userdata']:
                with open(player_data_path, 'w') as outfile:
                    profile_data1['userdata'][rep_author]['repped'] += 1
                    profile_data1['userdata'][chosen_user_rep]['rep'] += 1
                    json.dump(profile_data1, outfile)
                await bot.say(f':arrow_double_up: {rep_author_mention} has repped {chosen_user2}')
                await check_level(ctx)
        else:
            await bot.say('You already repped someone today')
    else:
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][credits_author] = {"daily":0, "credits":0, "level":1, "xp":0, "streak":0, "rep":0, "repped":1, "armour":"nothing", "defense":0, "weapon":"fist", "damage":1}
            json.dump(profile_data1, outfile)
        await bot.say(f'{rep_author_mention} has 0 credits!')

@bot.command(pass_context=True, aliases=["money", "currency", "credit"], description='show your credits')
async def credits(ctx):
    credits_author = str(ctx.message.author)
    credits_author_mention = ctx.message.author.mention
    with open(player_data_path, 'r') as profile_data:
        profile_data1 = json.load(profile_data)
    if credits_author in profile_data1['userdata']:
        user_credits = profile_data1['userdata'][credits_author]['credits']
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][credits_author]['xp'] += 1
            json.dump(profile_data1, outfile)
        await bot.say(f':credit_card: {credits_author_mention} has {user_credits} credits!')
        await check_level(ctx)
    else:
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][credits_author] = {"daily":0, "credits":0, "level":1, "xp":1, "streak":0, "rep":0, "repped":0, "armour":"nothing", "defense":0, "weapon":"fist", "damage":1}
            json.dump(profile_data1, outfile)
        await bot.say(f':credit_card: {credits_author_mention} has 0 credits!')

@bot.command(pass_context=True, aliases=["progress"], description='show your xp')
async def xp(ctx):
    xp_author = str(ctx.message.author)
    xp_author_mention = ctx.message.author.mention
    with open(player_data_path, 'r') as profile_data:
        profile_data1 = json.load(profile_data)
    if xp_author in profile_data1['userdata']:
        current_xp = profile_data1['userdata'][xp_author]['xp']
        await bot.say(f'{xp_author_mention} has {current_xp}/200xp!')
        await check_level(ctx)
    else:
        with open(player_data_path, 'r') as profile_data:
            profile_data1 = json.load(profile_data)
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][xp_author] = {"daily":0, "credits":0, "level":1, "xp":1, "streak":0, "rep":0, "repped":0, "armour":"nothing", "defense":0, "weapon":"fist", "damage":1}
            json.dump(profile_data1, outfile)
        await bot.say(f'{xp_author_mention} has 1/200xp!')

@bot.command(pass_context=True, description='show your level')
async def level(ctx):
    level_author = str(ctx.message.author)
    level_author_mention = ctx.message.author.mention
    with open(player_data_path, 'r') as profile_data:
        profile_data1 = json.load(profile_data)
    if level_author in profile_data1['userdata']:
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][level_author]['xp'] += 1
            json.dump(profile_data1, outfile)
        with open(player_data_path, 'r') as level_data:
            daily_data_level_check = json.load(level_data)
        if daily_data_level_check['userdata'][level_author]['xp'] >= 200:
            with open(player_data_path, 'w') as outfile:
                daily_data1['userdata'][level_author]['level'] += 1
                daily_data1['userdata'][level_author]['xp'] = 0
                json.dump(daily_data1, outfile)
            with open(player_data_path, 'r') as level_data:
                daily_data_level = json.load(level_data)
            daily_new_level = daily_data_level['userdata'][level_author]['level']
            await bot.say(f'{level_author_mention} is level {daily_new_level}!')
        else:
            with open(player_data_path, 'r') as level_data:
                daily_data_level = json.load(level_data)
            daily_new_level = daily_data_level['userdata'][level_author]['level']
            await bot.say(f'{level_author_mention} is level {daily_new_level}!')
    else:
        with open(player_data_path, 'r') as profile_data:
            profile_data1 = json.load(profile_data)
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][level_author] = {"daily":0, "credits":0, "level":1, "xp":1, "streak":0, "rep":0, "repped":0, "armour":"nothing", "defense":0, "weapon":"fist", "damage":1}
            json.dump(profile_data1, outfile)
        await bot.say(f'{level_author_mention} is level 1!')

@bot.command(pass_context=True, description='get your daily')
async def daily(ctx):
    daily_author = str(ctx.message.author)
    daily_author_mention = ctx.message.author.mention
    with open(player_data_path, 'r') as profile_data:
        daily_data1 = json.load(profile_data)
    if daily_author in daily_data1['userdata']:
        if daily_data1['userdata'][daily_author]['daily'] != 1:
            if daily_data1['userdata'][daily_author]['level'] <= 25:
                await bot.say(f'{daily_author_mention} got 200 credits for their daily')
                with open(player_data_path, 'w') as outfile:
                    daily_data1['userdata'][daily_author]['credits'] += 200
                    daily_data1['userdata'][daily_author]['daily'] += 1
                    daily_data1['userdata'][daily_author]['xp'] += 5
                    json.dump(daily_data1, outfile)
                await check_level(ctx)
            else:
                await bot.say(f'{daily_author_mention} got 250 credits for their daily')
                with open(player_data_path, 'w') as outfile:
                    daily_data1['userdata'][daily_author]['credits'] += 250
                    daily_data1['userdata'][daily_author]['daily'] += 1
                    daily_data1['userdata'][daily_author]['xp'] += 5
                    json.dump(daily_data1, outfile)
                await check_level(ctx)
        else:
            await bot.say('You redeemed your daily already')
    else:
        with open(player_data_path, 'r') as profile_data:
            profile_data1 = json.load(profile_data)
        with open(player_data_path, 'w') as outfile:
            profile_data1['userdata'][daily_author] = {"daily":1, "credits":200, "level":1, "xp":5, "streak":0, "rep":0, "repped":0, "armour":"nothing", "defense":0, "weapon":"fist", "damage":1}
            json.dump(profile_data1, outfile)
        await bot.say(f'{daily_author_mention} got 200 credits for their daily')


@bot.group(pass_context=True, description='find out if you or a friend is cool')
async def cool(ctx, chosen_user: discord.Member):
    cool_author = ctx.message.author.mention
    chosen_user2 = chosen_user.mention
    cool_message = await bot.say('{} wants to see if {} is cool'.format(cool_author, chosen_user2))
    await asyncio.sleep(1.7)
    cool_or_not_cool = [":cool:", "cool", "cool", "kinda cool", "just OK", "not cool"]
    random_cool_not_cool = '{} is {}'.format(chosen_user2, random.choice(cool_or_not_cool))
    await bot.edit_message(cool_message, random_cool_not_cool)
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True, aliases=["commands"], description='command list')
async def command(ctx):
    await bot.say('```md\n# Command List #\n```\n**Use prefix . when doing commands**\n**[Command Category]** Then list of commands in the categories\nUse .help [command] to find out how to use the command\nDo not include []\n**1. Core -** `highfive` `slap` `punch`\n**2. Economy - ** `daily` `credits` `level` `xp`\n**3. Dice - ** `d4` `d6` `d8` `d10` `d12` `d20` \n**4. Math - ** `add` `subtract` `multiply` `divide`\n')
    await check_level(ctx)

@bot.command(pass_context=True, aliases=["hi"])
async def hello(ctx):
    await bot.say('Hello! :speech_balloon:')
    await check_level(ctx)

@bot.command(pass_context=True, aliases=["join", "server", "invite"], description='Get link to invite Nihilus to your server')
async def website(ctx):
    await bot.say('The website for Nihilus\nhttps://nihilus--savagecoder77.repl.co/')
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True, description='add numbers')
async def add(ctx, first_number : float, second_number : float):
    await bot.say(first_number + second_number)
    await add_1_xp(ctx)
    await check_level(ctx)
@bot.command(pass_context=True, description='subtract numbers')
async def subtract(ctx, first_number : float, second_number : float):
    await bot.say(first_number - second_number)
    await add_1_xp(ctx)
    await check_level(ctx)
@bot.command(pass_context=True, description='multiply numbers')
async def multiply(ctx, first_number : float, second_number : float):
    await bot.say(first_number * second_number)
    await add_1_xp(ctx)
    await check_level(ctx)
@bot.command(pass_context=True, description='divide numbers')
async def divide(ctx, first_number : float, second_number : float):
    await bot.say(first_number / second_number)
    await add_1_xp(ctx)
    await check_level(ctx)
@bot.command(pass_context=True, aliases=["sqrt"], description='find square root of number')
async def squareroot(ctx, number : float):
    if number > 0:
        squarerooted_number = math.sqrt(number)
        await bot.say(squarerooted_number)
        await add_1_xp(ctx)
        await check_level(ctx)
    else:
        await bot.say('The number is negative or will give a nonreal number')
        await check_level(ctx)

@bot.command(pass_context=True, description='4 sided dice roll')
async def d4(ctx):
    roll_message = await bot.say('rolling ...')
    d4_roll = ["1", "2", "3", "4"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d4_roll))
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True, aliases=["dice"], description='dice roll')
async def d6(ctx):
    roll_message = await bot.say('rolling ...')
    d6_roll = ["1", "2", "3", "4", "5", "6"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d6_roll))
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True, description='8 sided dice roll')
async def d8(ctx):
    roll_message = await bot.say('rolling ...')
    d8_roll = ["1", "2", "3", "4", "5", "6", "7", "8"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d8_roll))
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True, description='10 sided dice roll')
async def d10(ctx):
    roll_message = await bot.say('rolling ...')
    d10_roll = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d10_roll))
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True, description='12 sided dice roll')
async def d12(ctx):
    roll_message = await bot.say('rolling ...')
    d12_roll = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d12_roll))
    await add_1_xp(ctx)
    await check_level(ctx)

@bot.command(pass_context=True)
async def d20(ctx):
    roll_message = await bot.say('rolling ...', description='20 sided dice roll')
    d20_roll = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "**20!!, Critical Hit**"]
    await asyncio.sleep(1)
    await bot.edit_message(roll_message, random.choice(d20_roll))
    await add_1_xp(ctx)
    await check_level(ctx)

file_path = os.path.join('/Users/savagecoder/Desktop/Programming/pass.json')
with open(file_path, 'r') as token_data:
    data = json.load(token_data)
    discord_token = data['discord_token']
bot.run(discord_token)
