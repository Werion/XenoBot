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
    # | Prawda czy Wyzwanie - Standard, Uproszczony| START -------------------------------------------------------------
    @commands.command(name="pcw", pass_context=True)
    async def pcw(self, ctx):
        prawda = [
            'Czy wierzysz w miłość?',
            'Z kim się ostatnio pokłóciłeś?',
            'Jakie są twoje ulubione kwiatki?',
            'Czy kiedykolwiek coś ukradłeś/aś?',
            'Czy uważasz się za osobę nieśmiałą?',
            'Co wolisz: psy czy koty?',
            'Czy kiedykolwiek ubierałeś bliznę płci przeciwnej?',
            'Jaka jest twoja ulubiona piosenka?',
            'Kiedy pierwszy raz się całowałeś/aś?',
            'Czego się boisz?',
            'Komu ostatnio powiedziałeś słowa „Kocham Cię”?',
            'Jakie jest Twoje ulubione imię?',
            'Z kim się ostatnio pokłóciłeś?',
            'Jeśli mógłbyś wybrać swoje imię, jakie by ono było?',
            'Wymień marki ciuchów, które masz na sobie',
            'Jaki najbardziej wyzywający strój zdarzyło Ci się ubrać?',
            'Czy miałeś robiony masaż? Jeżeli tak, to przez kogo?',
            'Czy Tomasz Hajto przejechał starą babe na pasach?',
            'Jak długo najdłużej siedziałeś/aś przed komputerem?',
            'Czy Werion jest dobrym programistą (spoiler: Tak!)',
            'Chciałbyś pocałować kogoś z obecnych tu osób?',

        ]

        wyzwanie = [
            'Wypij ocet',
            'Zjedz masło',
            'Wypierdol kota przez okno (a tak na serio to nie)',
            'Wejdź pod stół i zachrumkaj jak świnka',
            'Pocałuj w szyję osobę po Twojej prawej stronie',
            'Zrób 3 minutowy stand up',
            'Kręć się w lewo przez 30 sekund',
            'Weź długopis w usta i napisz coś na kartce',
            'Weś głęboki oddech i krzyknij „JEBAĆ DISA!” z całej siły',
            'Rzuć wszystko i wyjedź w Bieszczady',
            'Udawaj rewolwerowca z westeru',
            'Zapiej jak kogut',
            'Udawaj wybranego członka serwera discord na którym jesteś',
            'Obejrz Bocu no pico (czy jak się to pieze, nie będę googlował) i pochwal się swoimi doświeczeniami',
            'Naśladuj samochód',
            'Poliż klamkę',
            'Zagraj w Fortnite przez jedną godzinę',
            'Twerk-uj przez minutę',
            'Ułóż wiersz o Disie i zaprezentuj go wszystkim'
        ]

        embed = discord.Embed(title="Prawda czy Wyzwanie", description=f"{ctx.author.mention}", color=0xc0148c)
        embed.add_field(name="Prawda", value=f"{random.choice(prawda)}", inline=True)
        embed.add_field(name="Wyzwanie", value=f"{random.choice(wyzwanie)}", inline=True)
        embed.set_footer(text="XenoBeep")
        await ctx.send(embed=embed)

    # END --------------------------------------------------------------------------------------------------------------
    # | Prawda czy Wyzwanie - Error handling | START -------------------------------------------------------------------
    @pcw.error
    async def pcw_error(self, ctx, error):
        await ctx.send(f"`{error}`")
    # END --------------------------------------------------------------------------------------------------------------


def setup(client):
    client.add_cog(Fun(client))
