import os, requests, json, time, threading, random, string, base64, sys, asyncio
from itertools import cycle
from colorama import Fore
from discord.ext import commands
import random
import discord
from datetime import datetime, timezone

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.command()
async def token(ctx, userid):
    token = str(userid)
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    embed = discord.Embed(title="Token", description=bas64_bytes.decode('utf-8'), color=0x00ff00)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("hello")









bot.run(YOUR TOKEN)