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
    results = [dndice.verbose(expr) for expr in args]
    await context.send('; '.join(results))


with open('./app_token', 'r') as f:
    token = f.read().strip()
bot.run(token)
