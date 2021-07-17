import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
from cogs import vault
from utils import lang


class VaultLang(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Language: Ready")

    # Commands
    @commands.command(name="language", pass_context=True, aliases=['lang'])
    async def language(self, ctx):
        server = ctx.message.guild.id
        dictionary = lang.get(vault.guild_lang(server))
        lang_selected = vault.guild_lang(server)
        await ctx.send(f"{dictionary['lang_currently_using']} {lang_selected}")

    @commands.command(name="changelanguage", pass_context=True, aliases=['changelang', 'setlang'])
    async def change_language(self, ctx, mode=None):
        server = ctx.message.guild.id
        dictionary = lang.get(vault.guild_lang(server))
        list_lang = lang.list_lang()
        if mode is None:
            await ctx.send(f"{dictionary['list_of_lang']} {list_lang}")
            return
        if mode in list_lang:
            vault.write_lang_data(serverID=server, mode=mode)
            dictionary = lang.get(vault.guild_lang(server))
            await ctx.send(f"{dictionary['changed_lang']} {mode}")
        else:
            await ctx.send(f"{dictionary['invalid_lang']}")


def setup(client):
    client.add_cog(VaultLang(client))
