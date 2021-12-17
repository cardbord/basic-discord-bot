#all the imports required. some may be downloaded with discord.py 
import discord
from discord.ext import commands
import os
from discord.ext.commands import Bot
import asyncio
import random as r
from discord import utils


client = Bot(command_prefix=("sus!"), intents=discord.Intents.all()) #the prefix can be changed at any time, currently it is !sus (don't bully me for the among us reference).


@client.event
async def on_ready():
    print("Connected and ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="helo")) #custom 'watching' status


#just your average test command, nothing special
@client.command() #use client.command() to initiate a command
async def hello(ctx): #'hello' is my command here. with this prefix, calling the command would be 'sus!hello'. the parameter 'ctx' is nearly always needed for any command to work.
    await ctx.send("hey there!")


#demo of how to use the random module in a command
@client.command()
async def choose(ctx, arg1, arg2):
    choice = r.choice([arg1, arg2])
    await ctx.send(f"I choose {choice}.")


#a command that allows a specific member to be mentioned
@client.command()
async def avatar(ctx, *, user:discord.Member = None):
    if user is None:
        user = ctx.author
    ava = user.avatar_url
    embed=discord.Embed(title=f"{user.display_name}'s avatar!")
    embed.set_image(url=ava)
    await ctx.send(embed=embed)


#demo of how to use commands locked to certain roles
@client.command()
@commands.has_role("Starff") #you could also do @commands.has_permissions(permission)
async def purge(ctx, amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Purged {amount} messages in this channel.")



#if you want to make your bot respond to certain messages, you can use something like
@client.listen('on_message')
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    
    if msg.startswith('hello bot'):
        await message.channel.send(f"Hello there {message.author.display_name}, how's it going?")






TOKEN = ('') #copy bot token into these brackets, the bot token can be found on your bot's page on the discord developer website.
client.run(TOKEN) 