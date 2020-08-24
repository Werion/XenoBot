import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle


class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print("> Miscellaneous: Ready")

    # Commands
    @commands.command(name="w_dm", pass_context=True)
    async def w_dm(self, ctx, *, question):
        user = self.client.get_user(240117268745289729)
        await user.send(f'{ctx.author.mention}: {question}')
        await ctx.send(f'`Wysłano pytanie do {user}: {question}`')

    @commands.command(name="jd", pass_context=True)
    async def jd(self, ctx):
        await ctx.send(f'JD')

    @tasks.loop(seconds=10)
    async def change_status(self):
        status = cycle(['Wersja 0.0.5'])
        # status = f"{round(client.latency * 1000)}ms"
        await self.client.change_presence(activity=discord.Game(next(status)))


def setup(client):
    client.add_cog(Miscellaneous(client))
