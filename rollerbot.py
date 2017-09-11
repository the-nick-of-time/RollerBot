import re
import asyncio

import discord

import rolling as r

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    m = re.match('/(roll|r)\s*(.*)', message.content)
    if (m):
        result = r.roll(m.group(2), option='multipass')
        await client.send_message(message.channel, result)

client.run('MzU2ODU2Mzg4Nzg3MzcyMDMy.DJhjFg.gydjLkA-o43ZjX49j-_XiMPFx14')
