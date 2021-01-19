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

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def report(self, ctx, *, arg):
        channel = await self.bot.fetch_channel(801057319731462154) #this is the report channel id
        embed = discord.Embed(
            color = discord.Color(0xFFC270), title=f'New Report from **{ctx.author}**' , description = f"```yaml\n{arg}\n```\nReported from **{ctx.guild.name}**\n\nMember: {ctx.author.mention} | {ctx.author.id}" , timestamp=ctx.message.created_at)
        embed.set_author(
            name=f"{ctx.author.name}'s complaint ", icon_url=f'{ctx.author.avatar_url}')
        embed.set_thumbnail(url= ctx.author.avatar_url)
        await ctx.message.delete()
        await channel.send(embed=embed)
        
        #Sents the User a Message if the report/suggestion has been set or not
        rembed = discord.Embed(title = "" , description = f"{ctx.author.name} Your report has been sent to the Team! A Mod will be in while with you, Till then, Thanks for you report! It Helps us to Fix the Bug" , color = 0x5F3FD8)
        await ctx.send(embed = rembed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def suggest(self, ctx, *, arg):
        channel = await self.bot.fetch_channel(801057297841389631)
        embed = discord.Embed(
            color = discord.Color(0xFFC270), title=f'New Suggestion from **{ctx.author}**', description = f"```yaml\n{arg}\n```\nSuggestions from **{ctx.guild.name}**\n\nMember: {ctx.author.mention} | {ctx.author.id}" , timestamp=ctx.message.created_at)
        embed.set_author(
            name=f"{ctx.author.name}'s suggestion ", icon_url=f'{ctx.author.avatar_url}')
        embed.set_thumbnail(url= ctx.author.avatar_url)
        await ctx.message.delete()
        await channel.send(embed=embed)

        #Sents the User a Message if the report/suggestion has been set or not
        sembed = discord.Embed(title = "" , description = f"{ctx.author.name} Your suggestion has been sent to the Team! Soon we are gonna do some improve to it!, Till then, Thanks for you suggestion!! It Helps us to make feel the user Comfortable!" , color = 0x5F3FD8)
        await ctx.send(embed = sembed)

    @commands.command()
    async def setup(self, ctx):

        setup_channel = discord.utils.get(ctx.guild.text_channels, name=f'dylana-private')
        
        if setup_channel:
            await ctx.send(f'You already have an private channel {setup_channel.mention}')
            return
        
        else:    
            guild = ctx.guild
            member = ctx.author
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
            }
            channel = await guild.create_text_channel('dylana-private' ,  overwrites=overwrites)
            await ctx.message.add_reaction('<:CheckMark:789075069069950987>')
            embed = discord.Embed(title = "What is this channel for?",
                                description = "This Channel is made for **Regular Updates / Newsfeeds** about the Bot!. ```What will be sent here?\n- Changelogs\n- Bug fixes\n- Update logs\n- Official Giveaways\n- And Tons Of More```\n\n**Important Notes:**\n• Do not rename this channel.\n• You can test bot's commands here if you want to.\n\n**Important Links**\n[Support Server](https://discord.gg/jGrh2DmNbh)",
                                color = 0x5F3FD8)
            embed.set_footer(text = "Made by ❤️ MysT#9105")
            embed.set_author(name=f"{ctx.author}" , icon_url= ctx.author.avatar_url)
            await channel.send(embed = embed)


    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        ping_msg = await ctx.send("⚡ Loading... | ")
        await asyncio.sleep(0.1)
        await ping_msg.edit(content="⚡ Loading... /")
        await asyncio.sleep(0.1)
        await ping_msg.edit(content="⚡ Loading... -")
        await asyncio.sleep(0.1)
        await ping_msg.edit(content="⚡ Loading... \ ")
        await asyncio.sleep(0.1)
        await ping_msg.edit(content="⚡ Loading... |")
        await asyncio.sleep(0.1)
        await ping_msg.edit(content=f":ping_pong: Pong {ctx.author.mention}, {round(self.bot.latency*1000)} ms.")


    @commands.command()
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        Bot_version = 'v0.2'
        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='Here is a list of inforamtion About Dylana', colour=ctx.author.colour, timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=Bot_version)
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCount)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value=f"<@630629678121615401>")
        embed.add_field(name='Created At' , value=f"19/1/2021, On Tuesday, At 2:45 pm")

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f"Keep Jamming Out! ❤️ | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    
    @commands.command()
    async def invite(self, ctx):
        
        invite1 = "https://discord.com/oauth2/authorize?client_id=793041553684955166&scope=bot&permissions=2088234230"
        invite2 = "https://discord.com/oauth2/authorize?client_id=793041553684955166&scope=bot&permissions=2147483647"
        
        embed = discord.Embed(title = "Thank you for inviting Dylana <3" , description = f"[Dylana Invite Link (Recommended) ]({invite1})\n[Dylana Invite Link (Administrator) ]({invite2})" , color = 0x5F3FD8)
        embed.set_author(name = f"{ctx.author.name}" , icon_url=ctx.author.avatar_url)

        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(general(bot))