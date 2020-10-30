import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Admin module: Ready")

    # Commands
    #@commands.command(name="kick", pass_context=True)
    #@has_permissions(kick_members=True)
    #async def _kick(self, ctx, member: discord.Member, *, reason=None):
    #    await member.kick(reason=reason)
    #    await ctx.send(f'`Kicked {member.mention}`')

    #@_kick.error
    #async def kick_error(self, ctx, error, prefix):
    #    if isinstance(error, MissingPermissions):
    #        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    #        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    #    elif isinstance(error, commands.MissingRequiredArgument):
    #        embed = discord.Embed(title="Błąd", description="Nieprawidłowy syntax")
    #        embed.add_field(name="Użycie:", value=f"kick [nazwa]" " {powód}", inline=False)
    #        await ctx.send(embed=embed)

    #@commands.command(name="ban", pass_context=True)
    #@has_permissions(ban_members=True)
    #async def ban(self, ctx, member: discord.Member, *, reason=None):
    #    await member.ban(reason=reason, )
    #    await ctx.send(f'`Banned {member.mention}`')

    #@ban.error
    #async def ban_error(self, ctx, error, prefix):
    #    if isinstance(error, MissingPermissions):
    #        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    #        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    #    elif isinstance(error, commands.MissingRequiredArgument):
    #       await ctx.send(f'`Użycie: ban' + ' [Użyytkownik] {Powód}`')

    #@commands.command(name="unban", pass_context=True)
    #@has_permissions(ban_members=True)
    #async def unban(self, ctx, *, member):
    #    banned_users = await ctx.guild.bans()
    #    member_name, member_discriminator = member.split('#')

    #    for ban_entry in banned_users:
    #        user = ban_entry.user

    #       if (user.name, user.discriminator) == (member_name, member_discriminator):
    #          await ctx.guild.unban(user)
    #            await ctx.send(f'`Unbanned {user.mention}`')
    #            return

    #@unban.error
    #async def unban_error(self, error, ctx):
    #    if isinstance(error, MissingPermissions):
    #        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
    #        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    #    elif isinstance(error, commands.MissingRequiredArgument):
    #        await ctx.send('`Użycie: unban [Użyytkownik] {Powód}`')

    @commands.command(name="staff_dm", pass_context=True)
    @has_permissions(administrator=True)
    async def staff_dm(self, ctx, uid=int(), *, question):
        user = self.client.get_user(uid)
        await user.send(f'{ctx.author.mention}: {question}')
        await ctx.send(f'`Wysłano pytanie do .{user}: {question}`')

    @staff_dm.error
    async def staff_dm_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send('Panie, pan nie ma uprawnień by użyć tej komendy!')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'`Użycie: staff_dm' + ' [ID Uzytkownika Discord] [Tekst]`')
        else:
            ctx.sent(f"`{error}`")
            print(error)


def setup(client):
    client.add_cog(Admin(client))
