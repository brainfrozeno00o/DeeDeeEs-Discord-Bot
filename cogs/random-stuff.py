import discord
import random
from discord.ext import commands

class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # example of this would be input: "Mamatay ka na." -> output: "MaMatAy KA nA."
    @commands.command(name="memeify", aliases=["spongebob"], help="Spongebob loves you and me together.", description="What user inputs becomes a Spongebob version of the string.")
    async def memeify(self, context, *, input_string: str):
        output_string = []

        for char in input_string:
            cap = random.randint(0, 1)
            if cap:
                output_string.append(char.upper())
            else:
                output_string.append(char.lower())

        final_output = ''.join(output_string)

        await context.channel.send(f"{context.author.mention} {final_output}")
    
    @commands.command(name="roll", aliases=["lucky", "dice"], help="Just rolling a dice...", description="User inputs a number x to get a random number from 1-x. If no input, a standard six-sided dice will be rolled.")
    async def roll(self, context, limit: str):
        # strictly numeric only
        if limit.isnumeric():
            result = random.randint(1, int(limit))

            await context.channel.send(f"{context.author.mention} Oi gago, nakuha mo **{result}**")
        # as long as input is provided and it's not a number
        else:
            await context.channel.send(f"Hoy {context.author.mention}, hindi number nilagay mo tanga! Batukan kita dyan eh!")

def setup(bot):
    bot.add_cog(Random(bot))

'''
Mainly got code from this gist: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
API Documentation can be found here: https://discordpy.readthedocs.io/en/latest/
'''