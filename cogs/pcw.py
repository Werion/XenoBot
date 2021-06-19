import discord
from discord.ext import commands
# from discord.ext.commands import has_permissions, MissingPermissions
import random
import json


class PCW(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open('pcw.json', 'r', encoding='utf-8') as f:
            self.pcw_json = json.load(f)
            print("Loaded pcw data")

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> PCW module: Ready")

    # Command
    # | Prawda czy Wyzwanie - Standard, Uproszczony| START -------------------------------------------------------------
    @commands.command(name="pcw", pass_context=True)
    async def pcw(self, ctx):
        truth = self.pcw_json['truth']

        dare = self.pcw_json['dare']

        embed = discord.Embed(title="Prawda czy Wyzwanie", description=f"{ctx.author.mention}", color=0xc0148c)
        embed.add_field(name="Prawda", value=f"{random.choice(truth)}", inline=True)
        embed.add_field(name="Wyzwanie", value=f"{random.choice(dare)}", inline=True)
        embed.set_footer(text="XenoBeep")
        await ctx.send(embed=embed)

    # END --------------------------------------------------------------------------------------------------------------
    # | Prawda czy Wyzwanie - Error handling | START -------------------------------------------------------------------
    @pcw.error
    async def pcw_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    # END --------------------------------------------------------------------------------------------------------------
    # | Prawda czy Wyzwanie v2 - Standard, Losowane | START ------------------------------------------------------------
    @commands.command(name="pcwv2", pass_context=True)
    async def pcwv2(self, ctx):
        truth = self.pcw_json['truth']

        dare = self.pcw_json['dare']

        typ = [
            'Prawda',
            'Wyzwanie'
        ]

        losowanie = random.choice(typ)

        if losowanie == 'Prawda':
            embed = discord.Embed(title="Prawda czy Wyzwanie v2", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Prawda", value=f"{random.choice(truth)}", inline=True)
            embed.set_footer(text="XenoBeep")
            await ctx.send(embed=embed)
        elif losowanie == 'Wyzwanie':
            embed = discord.Embed(title="Prawda czy Wyzwanie v2", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Wyzwanie", value=f"{random.choice(dare)}", inline=True)
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
        truth = self.pcw_json['truth']

        dare = self.pcw_json['dare']

        if PorW == 'P':
            embed = discord.Embed(title="Prawda czy Wyzwanie v3", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Prawda", value=f"{random.choice(truth)}", inline=True)
            embed.set_footer(text="XenoBeep")
            await ctx.send(embed=embed)
        elif PorW == 'W':
            embed = discord.Embed(title="Prawda czy Wyzwanie v3", description=f"{ctx.author.mention}", color=0xc0148c)
            embed.add_field(name="Wyzwanie", value=f"{random.choice(dare)}", inline=True)
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
