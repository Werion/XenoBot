import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Experimental(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Experimental: Ready")

    # Commands
    @commands.command(name="say", pass_context=True)
    async def say(self, ctx, *, message):
        await ctx.send('<a:BlobRave:549235493909561346>')

    # END --------------------------------------------------------------------

    # | Respond on private messages | START ----------------------------------

    # @client.event
    # async def on_message(message):
    # we do not want the bot to reply to itself
    # if message.content.startswith("#dm"):
    # if message.author == client.user:
    #   return

    # can be cached...
    # await client.process_commands(message.channel, message.content[3:])
    # discordUser = message
    # await client.process_commands(message)
    # content = message
    # user = client.get_user(discordUser)
    # await user.send(content)
    # me = await client.get_user_info('437289250753347605')
    # await client.send_message(me, "Hello!")

    # END ----------------------------------------------------------------------


def setup(client):
    client.add_cog(Experimental(client))
