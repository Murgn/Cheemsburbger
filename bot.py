import discord
import ast
import json
import asyncio
import datetime
import time
import platform
from discord.ext import commands
from discord.utils import find
import random
import sysconfig
import sys
import os
from asyncio import sleep
import math

from tokens import BOT_TOKEN

TOKEN = BOT_TOKEN

client = commands.Bot(command_prefix = "!cb", case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'{client.user.name} is awake! - {client.user.id}')

@client.command()
async def ping(ctx):
    await ctx.send("BURBGERBEBBE")

@client.command(name="help")
async def _help(ctx):
    embed = discord.Embed(title="Help Command",  color=0xDFC39A)
    ignore = []
    cogs = [c for c in client.cogs.keys()]
    for i in ignore:
        if i in cogs:
            cogs.remove(i)
    cogs.sort()
    lower_cogs = [c.lower() for c in cogs]
    
    for cog in cogs:
        commands_list = client.get_cog(cogs[lower_cogs.index(cog.lower())]).get_commands()
        commands = ""
        for command in commands_list:
            commands += "`{0}`, ".format(command)
        embed.add_field(name=cog.capitalize(), value=commands[:-2], inline=False)
        commands = ""
    await ctx.send(embed=embed)
    
client.run(TOKEN)
