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
  
    
class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Oh no {ctx.author.mention} ! Looks like you have missed out an argument for this command" ,  color = discord.Colour.red())
            await ctx.send(embed = embed)
        
        elif isinstance(error,commands.MissingPermissions):
            embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Oh no {ctx.author.mention} ! Looks like you don't have permissions to use this command" ,  color = discord.Colour.red())
            await ctx.send(embed = embed)
        
        elif isinstance(error, commands.BotMissingPermissions): 
            embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Oh no {ctx.author.mention} ! Looks like I Dont have the permissions for this command" ,  color = discord.Colour.red())
            await ctx.send(embed = embed)
        
        elif isinstance(error, commands.BotMissingRole):
            embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Oh no {ctx.author.mention} ! Looks like I Dont have the roles for this command" ,  color = discord.Colour.red())
            await ctx.send (embed = embed)
        
        elif isinstance(error, commands.errors.NoPrivateMessage):
            embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Oh no {ctx.author.mention} ! Looks like the User has blocked me or has their DM's closed." ,  color = discord.Colour.red())
            await ctx.send (embed = embed)
        
        elif isinstance(error, commands.CommandOnCooldown):
            # If the command is currently on cooldown trip this
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Looks like the Command is in **cooldown**. Please Try again after **{int(s)} secs**" ,  color = discord.Colour.red())
                await ctx.send (embed = embed)
            elif int(h) == 0 and int(m) != 0:
                embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Looks like the Command is in **cooldown**. Please Try again after **{int(m)} mins** and **{int(s)} secs**" ,  color = discord.Colour.red())
                await ctx.send (embed = embed)
            else:
                embed = discord.Embed(title = '', description = f"<:AzError:785041510256214059> Looks like the Command is in **cooldown**. Please Try again after **{int(h)} hrs**, **{int(m)} **mins** and {int(s)} secs**  " ,  color = discord.Colour.red())
                await ctx.send (embed = embed)          
        
        elif isinstance(error, commands.CommandNotFound):
            pass

def setup(bot):
    bot.add_cog(errors(bot))