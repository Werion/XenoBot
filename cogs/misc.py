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
    @tasks.loop(seconds=10)
    async def change_status(self):
        status = cycle(['Wersja 1.0.0'])
        # status = f"{round(client.latency * 1000)}ms"
        await self.client.change_presence(activity=discord.Game(next(status)))


def setup(client):
    client.add_cog(Miscellaneous(client))
