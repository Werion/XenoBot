import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

        print("Init utility")

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Utility module: Ready")

    # Commands
    @commands.command(name="clear", pass_context=True)
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Błąd", description="Nieprawidłowy syntax")
            embed.add_field(name="Użycie:", value=f"clear [ilość]", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(administrator=True)
    async def ping(self, ctx):
        await ctx.send(f'`{round(self.client.latency * 1000)} ms`')

    @commands.command(pass_context=True)
    async def about(self, ctx, ):  # member: discord.Member):
        # avatar = discord.User.default_avatar_url
        embed = discord.Embed(title="XenoBeep", description="Kolejny bot do różnych zadań", color=0xc0148c)
        embed.set_author(name="Autor: Werion")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/avatars/646398082845769759/cc882961d69879bdd308add45dd38999.webp?size=128')
        # embed.set_thumbnail(url="{}".format(member.avatar_url(self)))
        # embed.add_field(name="", value=f"1234", inline=False)
        embed.set_footer(text=f"Wersja {self.client.version}")
        await ctx.send(embed=embed)

        # await client.send_message(channel, embed=embed)

    @about.error
    async def about_error(self, ctx, error):
        await ctx.send(f'`{error}`')

    # @commands.command(pass_context=True)
    # async def help(self, ctx):
    #     author = ctx.message.author
    #
    #     embed = discord.Embed(
    #         colour=discord.Colour.orange()
    #     )
    #     embed.set_author(name='XenoBeep')
    #     embed.add_field(name='.ping', value='Returns pong!', inline=False)
    #
    #     #await ctx.send(embed=embed)
    #     await author.send(embed=embed)
    #     await ctx.send(f'`Wysłano wiadomość prywatną`')


def setup(client):
    client.add_cog(Utility(client))
