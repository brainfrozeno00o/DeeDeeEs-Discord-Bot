import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
server = os.getenv("DISCORD_SERVER_1")

test_channel = os.getenv("CUSTOM_CHANNEL_1")

client = discord.Client()

@client.event
async def on_ready():
    # using the abstracted functions for finding the server
    # guild = discord.utils.find(lambda g: g.name == server, client.guilds)
    guild = discord.utils.get(client.guilds, name=server)

    print(
        f"{client.user} has connected to Discord!\n"
        f"{client.user} is currently connected to {guild.name} with server ID: {guild.id}"    
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f"Current Server Members: \n - {members}")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to this joke server!"
    )

@client.event
async def on_message(message):
    guild = discord.utils.get(client.guilds, name=server)

    if message.author == client.user:
        return

    sample_du30_quotes = [
        "Brrt brrt brrt",
        "Putang ina mo!",
        "May gahd I hate drugs!",
        "Change is coming."
    ]

    custom_channel = discord.utils.get(guild.channels, name=test_channel)

    if 'dds' in message.content.lower() and message.channel == custom_channel:
        response = random.choice(sample_du30_quotes)
        await message.channel.send(response)
        print(f'Successful response!')

client.run(token)