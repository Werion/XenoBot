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
    @commands.command(name="say", )
    async def say(self, arg: str, *, message: str):
        channel = self.client.get_channel(arg)
        await self.client.send_message(channel, message)

   #####################################################################################################################


    global commandsEnabled={}

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        commandsEnabled[str(guild.id)] = {}
        for cmd in self.client.commands:
            commandsEnabled[str(guild.id)][cmd.name] = True

    @commands.command
    @has_permissions(administrator=True)
    async def Toggle(self, ctx, command):
        try:
            commandsEnabled[str(self.client.guild.id)][cmd.name] = not commandsEnabled[str(self.client.clientguild.id)][self.client.cmd.name]
            await ctx.send(f"{command} command {['disabled', 'enabled'][int()]}")
        except KeyError:
            await ctx.send(":x:Command with that name not found")

    @commands.command
    async def Example(self, ctx):
        if not commandsEnabled[str(ctx.guild.id)]["Example"]:
            await ctx.send(":x:This command has been disabled")
            return
        await ctx.send("Hello world!")

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
