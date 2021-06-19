from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class PVMSG(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Private message handler module: Ready")

    #commands.Cog.listener()
    #async def on_message(self, message):
    #    # you'll need this because you're also using cmd decorators
    #    await self.client.process_commands(message)
    #    if not message.guild:
    #        await message.author.send(f"Received: {message.content}")

    # Commands


def setup(client):
    client.add_cog(PVMSG(client))
