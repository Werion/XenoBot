import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Fun module: Ready")

    # Commands

    # | 8 Ball | START -------------------------------------------------------------------------------------------------
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
            'To pewne.',
            'Tak jest zdecydowanie.',
            'Bez wątpienia.',
            'Tak - napewno',
            'Możesz na tym polegać.',
            'Tak, jak widzę, tak.',
            'Najprawdopodobniej.',
            'Chyba tak.',
            'Tak.',
            'Znaki wskazują na tak.',
            'Zdania ekspertow sa podzielone.',
            'Odpowiedź mglista, spróbuj ponownie.',
            'Zapytaj ponownie później.',
            'Lepiej ci teraz nie mówić.',
            'Nie można teraz przewidzieć.',
            'Skoncentruj się i zapytaj ponownie.',
            "Nie licz na to.",
            'Moja odpowiedź brzmi nie.',
            'Moje źródła mówią nie.',
            'Perspektywa niezbyt dobra.',
            'Bardzo wątpliwe.',

        ]
        # await ctx.send(f"{ctx.message.author}\nPytanie: {question}\nOdpowiedź: {random.choice(responses)}")
        await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")

    # END --------------------------------------------------------------------------------------------------------------
    # | 8 Ball - Error handling | START --------------------------------------------------------------------------------
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send('Panie, pan nie ma uprawnień by użyć tej komendy!')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'`Użycie: 8ball' + ' [pytanie]`')

    # END --------------------------------------------------------------------------------------------------------------




def setup(client):
    client.add_cog(Fun(client))
