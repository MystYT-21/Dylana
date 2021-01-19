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



class extentions(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, module_name = None):
        
        try:
            if module_name is None:
                await ctx.send(f"Hey {ctx.author.mention}, Enter the Module name so that I can do the Actions.")
            else:
                self.bot.load_extension(f"cogs.{module_name}")
                embed2 = discord.Embed(title='', description = f"{module_name} Module Loaded Successfully!"  , colour=0x5F3FD8, timestamp=ctx.message.created_at)
                embed2.set_author(name = f"{ctx.author}" , icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed2)
        except:
            embed3 = discord.Embed(title="", description = f"Failed To load {module_name} Module!" , colour=0x5F3FD8, timestamp=ctx.message.created_at)
            embed3.set_author(name = f"{ctx.author}" , icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed3)


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, module_name = None):

        try:
            if module_name is None:
                await ctx.send(f"Hey {ctx.author.mention}, Enter the Module name so that I can do the Actions.")
            else:
                self.bot.unload_extension(f"cogs.{module_name}")
                embed2 = discord.Embed(title='', description = f"{module_name} Module Unloaded Successfully!"  , colour=0x5F3FD8, timestamp=ctx.message.created_at)
                embed2.set_author(name = f"{ctx.author}" , icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed2)
        except:
            embed3 = discord.Embed(title="", description = f"Failed To Unload {module_name} Module!" , colour=0x5F3FD8, timestamp=ctx.message.created_at)
            embed3.set_author(name = f"{ctx.author}" , icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed3)


def setup(bot):
    bot.add_cog(extentions(bot))