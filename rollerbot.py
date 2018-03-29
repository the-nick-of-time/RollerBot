#!/usr/bin/env python3

import re
import asyncio

import discord

import rolling as r

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
def on_message(message):
    m = re.match('/(roll|r)\s*(.*)', message.content)
    if (m):
        results = []
        for expr in m.group(2).split():
            results.append(str(r.roll(expr, option='multipass')))
        result = '; '.join(results)
        yield from client.send_message(message.channel, result)

with open('./app_token', 'r') as f:
    token = f.read().strip()
client.run(token)
