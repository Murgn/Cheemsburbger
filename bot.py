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
PREFIX = "!cb"

client = commands.Bot(command_prefix = "!cb", case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'{client.user.name} is awake! - {client.user.id}')

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == "<@!778661276816769054>":
        await message.channel.send(f"Hi {message.author.mention}! :purple_heart:\nMy prefix is `{PREFIX}`!")

@client.command()
async def ping(ctx):
    await ctx.send("BURBGERBEBBE")

    
client.run(TOKEN)
