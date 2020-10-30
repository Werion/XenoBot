import discord
from discord.ext import commands
# from discord.ext.commands import has_permissions, MissingPermissions
import random


class PCW(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> PCW module: Ready")

    # Command
    # | Prawda czy Wyzwanie v2 - Standard, Losowane | START ------------------------------------------------------------
    @commands.command(name="pcwv2", pass_context=True)
    async def pcwv2(self, ctx):
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

        typ = [
            'Prawda',
            'Wyzwanie'
        ]

        losowanie = random.choice(typ)

        if losowanie == 'Prawda':
            embed = discord.Embed(title="Prawda czy Wyzwanie v2", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Prawda", value=f"{random.choice(prawda)}", inline=True)
            embed.set_footer(text="XenoBeep")
            await ctx.send(embed=embed)
        elif losowanie == 'Wyzwanie':
            embed = discord.Embed(title="Prawda czy Wyzwanie v2", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Wyzwanie", value=f"{random.choice(wyzwanie)}", inline=True)
            embed.set_footer(text="XenoBeep")
            await ctx.send(embed=embed)

    # END --------------------------------------------------------------------------------------------------------------
    # | Prawda czy Wyzwanie - Error handling | START -------------------------------------------------------------------
    @pcwv2.error
    async def pcw_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    # END --------------------------------------------------------------------------------------------------------------
    # | Prawda czy Wyzwanie v3 - Standard, Wybór | START ---------------------------------------------------------------
    @commands.command(name="pcwv3", pass_context=True)
    async def pcwv3(self, ctx, PorW):
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
            'Jak bardzo jebiesz disa?',
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

        if PorW == 'P':
            embed = discord.Embed(title="Prawda czy Wyzwanie v3", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Prawda", value=f"{random.choice(prawda)}", inline=True)
            embed.set_footer(text="XenoBeep")
            await ctx.send(embed=embed)
        elif PorW == 'W':
            embed = discord.Embed(title="Prawda czy Wyzwanie v3", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Wyzwanie", value=f"{random.choice(wyzwanie)}", inline=True)
            embed.set_footer(text="XenoBeep")
            await ctx.send(embed=embed)

    # END --------------------------------------------------------------------------------------------------------------
    # | Prawda czy Wyzwanie - Error handling | START -------------------------------------------------------------------
    @pcwv3.error
    async def pcw_error(self, ctx, error):
        await ctx.send(f"`{error}`")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"`Nie dałeś argumentu: P - Prawda | W - Wyzwanie`")
    # END --------------------------------------------------------------------------------------------------------------


def setup(client):
    client.add_cog(PCW(client))
