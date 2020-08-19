import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
server = os.getenv("DISCORD_SERVER_1")

test_channel = os.getenv("CUSTOM_CHANNEL_1")

# client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    # using the abstracted functions for finding the server
    # guild = discord.utils.find(lambda g: g.name == server, client.guilds)
    guild = discord.utils.get(bot.guilds, name=server)

    print(
        f"{bot.user} has connected to Discord!\n"
        f"{bot.user} is currently connected to {guild.name} with server ID: {guild.id}"    
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f"Current Server Members: \n - {members}")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Oi {member.name}, putang ina mong burat ka!"
    )

@bot.event
async def on_message(message):
    guild = discord.utils.get(bot.guilds, name=server)

    if message.author == bot.user:
        return

    swear_words = [
        "Shit",
        "Fuck",
        "Bullshit",
        "Putang ina mo",
        "Tarantado"
    ]

    custom_channel = discord.utils.get(bot.get_all_channels(), name=test_channel)

    if any(swear.lower() in message.content for swear in swear_words) and message.channel == custom_channel:      
        await message.channel.send(f"Hoy putang ina mong hinayupak ka! Ako lang pwede magmura dito gago.")

    await bot.process_commands(message)

@bot.command(name="dds", help="Get random meanings of DDS.")
async def dds(context):

    dds_meanings = [
        "So are you a Dingdong Dantes Supporter?",
        "So are you a Duterte Diehard Supporter?",
        "So are you a Dirty Dick Supporter?",
        "So are you part of the Davao Death Squad?",
        "You the Distributed Denial of Service, is it?"
    ]

    response = random.choice(dds_meanings)

    custom_channel = discord.utils.get(bot.get_all_channels(), name=test_channel)

    if custom_channel == context.channel:
        await context.channel.send(f"{response} <@{context.author.id}>")

@bot.command(name="digong", help="Get random quotes from our Daddy D.")
async def digong(context):

    sample_du30_quotes = [
        "Brrt brrt brrt",
        "Putang ina mo!",
        "May gahd I hate drugs!",
        "Change is coming."
    ]
    
    response = random.choice(sample_du30_quotes)

    custom_channel = discord.utils.get(bot.get_all_channels(), name=test_channel)

    if custom_channel == context.channel:
        await context.channel.send(f"{response} <@{context.author.id}>")
        
# client.run(token)
bot.run(token)