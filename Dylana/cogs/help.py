#Discord Modules: 1
import discord #for discord
from discord import Embed #for discord

from discord.ext import commands, tasks #for discord 
from discord.utils import get #for discord utility
from discord.voice_client import VoiceClient #for music
from discord.ext.commands import BucketType, cooldown #for cooldown

#Functions and File Storing: 2
import itertools
from itertools import cycle #For recycling status etc:
import asyncio #functions and etc
import aiohttp
import json #for file storing data

#Other Small Functions: 3
import requests
import traceback
import os
import sys
import datetime
import functools
import logging
import platform
import random
from datetime import datetime

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Dylana - Help" , description = "Hi, I am Dylana, a Music Bot! My default prefix is `d!` and `d?`.\n\n​To get started, join a voice channel and `d!play` a song. You can use song names, video links, and playlist links from YouTube!." , color = discord.Color(0xFFC270))
        embed.add_field(name = "General Commands" , value = "`ping`, `report`, `suggest`, `stats`, `invite`" , inline = False)
        embed.add_field(name="Music Commands" , value="`connect`, `equalizer`,  `nowplaying`, `pause`, `play`, `queue`, `resume`, `shuffle`, `skip`, `stop`, `swapdj`, `volume`" , inline = False)
        embed.add_field(name="Keep in Mind!" , value="More Commands will be Available soon! Thanks for being with us!")
        embed.set_author(name=f"{ctx.author.name}" , icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(help(bot))