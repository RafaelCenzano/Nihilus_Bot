
import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.messages'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('.wake'):
        messages = ["Where's that snooze button", "AHHHHHHH!!!!\nThat was a horrible dream", "I hate my alarm that bastard", "I'll be there soon\n*yawn*\nlike in one second"]
        await client.send_message(message.channel, random.choice(messages))

    elif message.content.startswith('.sleep'):
        await client.send_message(message.channel, 'Sleeping')
        await asyncio.sleep(2.5)
        await client.send_message(message.channel, 'zzzz')
        await asyncio.sleep(2.5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('.command'):
        await client.send_message(message.channel, '```md\n# Command List #\n```\n**Use prefix . when doing commands**\n**[Command Category]** Then list of commands in the categories\n**1. Core -** `messages`\n**2. Dice - ** `d4` `d6` `d8` `d10` `d12` `d20`\n**3. Misc - ** `wake` `sleep`')

#    elif message.content.startswith('.help'):
#        await client.send_message(message.channel, 'Use prefix . when running commands\n.help to access this page')

    elif message.content.startswith('.d4'):
        roll_message = await client.send_message(message.channel, 'rolling ...')
        d4_roll = ["1", "2", "3", "4"]
        await asyncio.sleep(1)
        await client.edit_message(roll_message, random.choice(d4_roll))
    elif message.content.startswith('.d6'):
        roll_message = await client.send_message(message.channel, 'rolling ...')
        d6_roll = ["0", "1", "2", "3", "4", "5", "6"]
        await asyncio.sleep(1)
        await client.edit_message(roll_message, random.choice(d6_roll))
    elif message.content.startswith('.d8'):
        roll_message = await client.send_message(message.channel, 'rolling ...')
        d8_roll = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        await asyncio.sleep(1)
        await client.edit_message(roll_message, random.choice(d8_roll))
    elif message.content.startswith('.d10'):
        roll_message = await client.send_message(message.channel, 'rolling ...')
        d10_roll = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        await asyncio.sleep(1)
        await client.edit_message(roll_message, random.choice(d10_roll))
    elif message.content.startswith('.d12'):
        roll_message = await client.send_message(message.channel, 'rolling ...')
        d12_roll = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        await asyncio.sleep(1)
        await client.edit_message(roll_message, random.choice(d12_roll))
    elif message.content.startswith('.d20'):
        roll_message = await client.send_message(message.channel, 'rolling ...')
        d20_roll = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20, Critical!!!"]
        await asyncio.sleep(1)
        await client.edit_message(roll_message, random.choice(d20_roll))

    elif message.content.startswith('.highfive'):
        embed.set_image(url='http://cdn.smosh.com/wp-content/uploads/2016/01/high-five-mass-fives.gif')
#        #await client.send_message(gif)
#    elif message.content.startswith('.slap' [player] ):
#        await client.send_message(message.channel, '**{} has been slapped**').format(player)
#        embed.set_image(url='https://i.makeagif.com/media/10-30-2015/Up5MqS.gif')

client.run('token')
