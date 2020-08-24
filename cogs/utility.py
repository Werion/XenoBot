import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

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
    async def ping(self, ctx):
        await ctx.send(f'`{round(self.client.latency * 1000)} ms`')

    @commands.command(pass_context=True)
    async def about(self, ctx):
        embed = discord.Embed(title="Xeno Beep", description="description")
        embed.set_author(name="Autor: Werion", )
        # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/646398082845769759/886b06c4dee4c4d487493c83a79751a3.png")
        embed.add_field(name="Test", value="1234", inline=False)
        embed.set_footer(text="version 0.0.5")
        await ctx.send(embed=embed)

        # await client.send_message(channel, embed=embed)


def setup(client):
    client.add_cog(Utility(client))
