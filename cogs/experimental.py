from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import time


class Experimental(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Experimental: Ready")

    # Commands
    @commands.command(name="error", pass_context=True)
    async def error(self, ctx):
        # It's entire purpose is to create an error

        # var1 = 'Test'
        await ctx.send(f'`{var1}`')

    @commands.command(name="w_dm", pass_context=True)
    async def w_dm(self, ctx, *, question):
        user = self.client.get_user(240117268745289729)
        await user.send(f'{ctx.author.mention}: {question}')
        await ctx.send(f'`Wysłano pytanie do {user}: {question}`')

    @commands.command(name="jd", pass_context=True)
    async def jd(self, ctx):
        await ctx.send(f'JD')

    @has_permissions(administrator=True)
    @commands.command(name="say", )
    async def say(self, arg: str, *, message: str):
        channel = self.client.get_channel(arg)
        await self.client.send_message(channel, message)

    @commands.command(name='raid')
    @has_permissions(administrator=True)
    async def raid(self, ctx, uid=int(), rep_time=int()):
        options = [
            'Zabij się',
            'Twoje życie nie ma sensu',
            'Pisowska kurwa!',
            'xDDDDDDDDDD',
            'Czy życie ci nie miłe?',
            'Why are you gey?',
            'Despacito',
            'PornHub - idź i płacz jak inni ruchają a nie ty :)',
            'Chyba podzielili ciebie przez 0, dlatego wyglądasz jak gówno',
            'Słyszałeś o tokenach uzytkownika?',
            'Pewien mądry człowiek ppowiedział: Kozak w necie, ale pizda w świecie',
            'Czy chcesz popełnić samobójstwo?',
            'Usziądź mni na mordzie',
            'Rucham ci matkę',
            'Potnij się ziemniakiem',
            'Pierdolony syf',
            'Pierdolony sukinsyn',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'UwU',
            'OwO',
            'Spierdalaj',
            'Idź poderwać swoją matkę',
            'Wypierdalaj',
            '',
        ]
        if uid == 1:
            await ctx.send(f'Request by: {ctx.author.mention}')
            await ctx.send(f'`Printing lib of words on channel`')
            await ctx.send(f'`{options}`')
        else:
            user_dc = self.client.get_user(uid)
            for counter in range(0, rep_time):
                message = random.choice(options)
                await user_dc.send(f'{message}')
                await ctx.send(f'`Dm raid on user {user_dc}: {counter + 1}||{rep_time}`')
                await ctx.send(f'`Showed msg: {message}`')

    @raid.error
    async def raid_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send('Panie, pan nie ma uprawnień by użyć tej komendy!')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'`Użycie: raid' + ' [id_użytkownika||print_debug]' + ' [liczba wiadomości]`')
        else:
            await ctx.send(f'{error}')


#####################################################################################################################


#  global commandsEnabled={}

#  @commands.Cog.listener()
#  async def on_guild_join(self, guild):
#      commandsEnabled[str(guild.id)] = {}
#      for cmd in self.client.commands:
#         commandsEnabled[str(guild.id)][cmd.name] = True

#  @commands.command
#  @has_permissions(administrator=True)
#  async def Toggle(self, ctx, command):
#      try:
#          commandsEnabled[str(self.client.guild.id)][cmd.name] = not commandsEnabled[str(self.client.clientguild.id)][self.client.cmd.name]
#          await ctx.send(f"{command} command {['disabled', 'enabled'][int()]}")
#      except KeyError:
#          await ctx.send(":x:Command with that name not found")

# @commands.command
#  async def Example(self, ctx):
#      if not commandsEnabled[str(ctx.guild.id)]["Example"]:
#          await ctx.send(":x:This command has been disabled")
#          return
#      await ctx.send("Hello world!")

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
