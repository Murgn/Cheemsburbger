import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print ("cheems is working.")

    @commands.command()
    async def example(self, ctx):
        await ctx.send("cheemsburbger")


def setup(client):
    client.add_cog(Fun(client))