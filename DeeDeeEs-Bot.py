import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
server = os.getenv("DISCORD_SERVER_1")

test_channel = os.getenv("CUSTOM_CHANNEL_1")

extensions = [
    "cogs.du30",
    "cogs.random-stuff"
]

# client = discord.Client()
bot = commands.Bot(command_prefix="!", description="Duterte Bot Example")

@bot.event
async def on_ready():
    # using the abstracted functions for finding the server
    # guild = discord.utils.find(lambda g: g.name == server, client.guilds)
    guild = discord.utils.get(bot.guilds, name=server)

    # this just prints if the bot has successfully got online in the server
    print(
        f"{bot.user} has connected to Discord!\n"
        f"{bot.user} is currently connected to {guild.name} with server ID: {guild.id}"    
    )

    # just prints the current members
    members = '\n - '.join([member.name for member in guild.members])
    print(f"Current Server Members: \n - {members}")

    # 0 = playing, 1 = streaming, 2 = listening, 3 = watching
    await bot.change_presence(activity=discord.Streaming(name="Jakol Simulator v6.9", url="https://www.twitch.tv/pokimane"))

# this happens when a new member joins the guild / server
@bot.event
async def on_member_join(member):
    #this dms the user
    await member.create_dm()
    await member.dm_channel.send(
        f"Oi {member.mention}, putang ina mong burat ka!"
    )

    # this sends a message to the general channel
    general_channel = discord.utils.get(bot.get_all_channels(), name="general")

    await general_channel.send(f"Jakol tayo pre {member.mention}")

# this happens when a member updates their status / activity / nickname / role
@bot.event
async def on_member_update(before, after):
    # do this if a member becomes online from being offline
    # can also be before.status = discord.Status.online and after.status == discord.Status.online
    if str(before.status) == "offline" and str(after.status) == "online":
        # this dms the user
        await after.create_dm()
        await after.dm_channel.send(
            f"Nandyan ka na pala burat ka!"
        )

# this happens when a member sends a message on any channel
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

# handling command errors, only have put if there is no input in a command where inputs are needed
@bot.event
async def on_command_error(context, exception):
    if isinstance(exception, commands.MissingRequiredArgument):
        # doing this just to avoid the empty string message issue
        response = f"Anong ginagawa mo?"
        
        if context.command.name == "roll":
            # do the standard roll from 1, 6 and show an angry message
            result = random.randint(1, 6)
            response = f"Tang ina mo ka {context.author.mention} wala kang nilagay! Eto nakuha mo **{result}** pakyu."
        elif context.command.name == "memeify":
            # send his favorite brrt brrt shit...
            response = f"BrRT bRrt bbRT bbrt..."

        await context.channel.send(f"{response}")

    raise exception

if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)
        
# client.run(token)
bot.run(token, bot=True, reconnect=True)

'''
Basics found here: https://realpython.com/how-to-make-a-discord-bot-python/
Mainly got code from this gist: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
API Documentation can be found here: https://discordpy.readthedocs.io/en/latest/
'''