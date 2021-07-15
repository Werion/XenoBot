import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import json
from cogs import vault

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open('lotto.json', 'r', encoding='utf-8') as f:
            self.lotto_json = json.load(f)
            print("Loaded lotto data")

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
    # Lotto | START ----------------------------------------------------------------------------------------------------
    @commands.command()
    async def lotto(self, ctx):
        # Get 6 numbers between  1 and 40
        lotto = [random.randint(1, 40) for a in range(6)]

        # Check the amounts of certain number in lotto variable
        count1 = sum(map(lambda x: x == 1, lotto))  # How many ones
        count2 = sum(map(lambda x: x == 2, lotto))  # How many twos
        count3 = sum(map(lambda x: x == 3, lotto))  # How many threes
        count4 = sum(map(lambda x: x == 4, lotto))  # etc ....
        count5 = sum(map(lambda x: x == 5, lotto))  # etc ....
        count6 = sum(map(lambda x: x == 6, lotto))  # etc ....

        # Shit way to sum all the values into one
        prize = count1 * self.lotto_json['1'] + count2 * self.lotto_json['2'] + count3 * self.lotto_json['3'] + count4 * \
                self.lotto_json['4'] + count5 * self.lotto_json['5'] + count6 * self.lotto_json['6']

        # data = vault.load_data()
        # user = ctx.message.author.id
        # server = ctx.message.guild.id
        # vault.add_data(userID=user, serverID=server, mode="Wallet", amount=prize)
        # Debug shit
        # await ctx.send(f'`DEBUG:'
        #                f'{lotto}\n'
        #                f'{count1}'
        #                f'{count2}'
        #                f'{count3}'
        #                f'{count4}'
        #                f'{count5}'
        #                f'{count6}'
        #                f'{prize}`'
        #                )
        # Win message
        await ctx.send(f'Wygrałeś {prize} zł')


def setup(client):
    client.add_cog(Fun(client))
