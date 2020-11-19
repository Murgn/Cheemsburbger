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

@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)
    print(error)    
    
@client.command()
async def ping(ctx):
    await ctx.send("BURBGERBEBBE")

    
client.run(TOKEN)
