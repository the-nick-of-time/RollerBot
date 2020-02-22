#!/usr/bin/env python3

from discord.ext import commands

import dndice

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def roll(context: commands.Context, *args):
    results = []
    for expr in args:
        try:
            results.append(dndice.verbose(expr))
        except dndice.RollError as e:
            results.append(str(inner_exception(e)))
    await context.send('; '.join(results))


def inner_exception(ex: dndice.RollError):
    current = ex
    while current.__cause__ is not None:
        current = current.__cause__
    return current


with open('./app_token', 'r') as f:
    token = f.read().strip()
bot.run(token)
