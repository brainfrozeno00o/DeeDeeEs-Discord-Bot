import discord
import random
from discord.ext import commands

class Duterte(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dds", aliases=['change'], help="Daghang salamat sa imong suporta...", description="Get random meanings of DDS.")
    async def dds(self, context):
        dds_meanings = [
            "So are you a Dingdong Dantes Supporter?",
            "So are you a Duterte Diehard Supporter?",
            "So are you a Dirty Dick Supporter?",
            "So are you part of the Davao Death Squad?",
            "You the Distributed Denial of Service, is it?"
        ]

        response = random.choice(dds_meanings)

        await context.channel.send(f"{response} {context.author.mention}")

    @commands.command(name="digong", aliases=["dugong"], help="Mahal na mahal ka ng Diyos.", description="Get random quotes from our Daddy D.")
    async def digong(self, context):
        sample_du30_quotes = [
            "Brrt brrt brrt",
            "Putang ina mo!",
            "May gahd I hate drugs!",
            "Change is coming."
        ]
        
        response = random.choice(sample_du30_quotes)

        await context.channel.send(f"{response} {context.author.mention}")

def setup(bot):
    bot.add_cog(Duterte(bot))

'''
Mainly got code from this gist: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
API Documentation can be found here: https://discordpy.readthedocs.io/en/latest/
'''