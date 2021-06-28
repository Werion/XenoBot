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
        # status = cycle([f'Wersja {self.client.version}'])
        status = cycle([f'Wersja {self.client.version}'])
        # status = f"{round(client.latency * 1000)}ms"
        await self.client.change_presence(activity=discord.Game(next(status)))

    @commands.command(name="toggle", description="Enable or disable a command!")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)

        if command is None:
            await ctx.send("I can't find a command with that name!")

        elif ctx.command == command:
            await ctx.send("You cannot disable this command.")

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"I have {ternary} {command.qualified_name} for you!")


def setup(client):
    client.add_cog(Miscellaneous(client))
