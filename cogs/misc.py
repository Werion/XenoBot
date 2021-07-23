import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle
from utils import lang
from cogs import vault


class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.change_status()
        print("> Miscellaneous: Ready")

    # Commands
    # @tasks.loop(seconds=10)
    async def change_status(self):
        # status = cycle([f'Wersja {self.client.version}'])
        status = f'{self.client.version}'
        # status = f"{round(client.latency * 1000)}ms"
        await self.client.change_presence(activity=discord.Game(status))

    @commands.command(name="toggle", description="Enable or disable a command!")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)
        guild = ctx.message.guild.id
        dictionary = lang.get(vault.guild_lang(guild))
        if command is None:
            await ctx.send(f"{dictionary['errors']['cannot_find']} {command}!")

        elif ctx.command == command:
            await ctx.send(f"{dictionary['errors']['cannot_disable']}")

        else:
            command.enabled = not command.enabled
            ternary = dictionary['toggle']['enabled'] if command.enabled else dictionary['toggle']['disabled']
            await ctx.send(
                f"{dictionary['toggle']['1']} {command.qualified_name} {dictionary['toggle']['2']} {ternary}")


def setup(client):
    client.add_cog(Miscellaneous(client))
