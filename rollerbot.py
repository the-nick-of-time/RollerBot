#!/usr/bin/env python3

import re
import asyncio

import discord

import dndice

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
@asyncio.coroutine
def on_message(message: discord.Message):
    m = re.match(r'/(roll|r)\s*(.*)', message.content)
    if m:
        results = []
        for expr in m.group(2).split():
            results.append(dndice.verbose(expr))
        result = '; '.join(results)
        yield from message.channel.send(result)


with open('./app_token', 'r') as f:
    token = f.read().strip()
client.run(token)
