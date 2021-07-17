import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
from utils import lang


def load_data():
    with open("vault.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_data(new_data, serverID, userID, mode):
    data = load_data()
    data["Economy"][str(serverID)][str(userID)][str(mode.title())] = int(new_data)
    with open('vault.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def write_lang_data(serverID, mode):
    data = load_data()
    data["Language"][str(serverID)] = mode
    with open('vault.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_lang_data():
    data = load_data()
    language = data["Language"]
    return language


def guild_lang(guild):
    guild = str(guild)
    data = load_lang_data()
    language = data[str(guild)]
    return language


def add_user(serverID, userID):
    data = load_data()
    data['Economy'][str(serverID)][str(userID)] = {"Bank": 0, "Wallet": 0}
    with open("vault.json", "w") as f:
        json.dump(data, f, indent=4)


def set_data(userID, serverID, mode, amount):
    data = load_data()
    if not str(userID) in data["Economy"][str(serverID)]:
        add_user(serverID=serverID, userID=userID)
        data = load_data()
    write_data(new_data=int(amount), serverID=str(serverID), userID=str(userID), mode=str(mode))


def add_data(userID, serverID, mode, amount):
    data = load_data()
    if not str(userID) in data["Economy"][str(serverID)]:
        add_user(serverID=serverID, userID=userID)
        data = load_data()
    new_data = int(data["Economy"][str(serverID)][str(userID)][str(mode.title())]) + int(amount)
    write_data(new_data=int(new_data), serverID=str(serverID), userID=str(userID), mode=str(mode))


def subtract_data(userID, serverID, mode, amount):
    data = load_data()
    if not str(userID) in data["Economy"][str(serverID)]:
        add_user(serverID=serverID, userID=userID)
        data = load_data()
    new_data = int(data["Economy"][str(serverID)][str(userID)][str(mode.title())]) - int(amount)
    write_data(new_data=int(new_data), serverID=str(serverID), userID=str(userID), mode=str(mode))


def check_user(userID, serverID):
    data = load_data()
    if not str(userID) in data["Economy"][str(serverID)]:
        return False
    else:
        return True


class Vault(commands.Cog):

    def __init__(self, client):
        print("Initialization of Economy module")
        self.client = client
        self.vault = load_data()
        print("Vault data loaded")

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("> Economy module: Ready")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.vault = load_data()
        if not str(guild.id) in self.vault["Economy"]:
            data = load_data()
            data['Economy'][str(guild.id)] = {}
            with open("vault.json", "w") as f:
                json.dump(data, f, indent=4)
        if not str(guild.id) in self.vault["Language"]:
            data = load_data()
            data['Language'][str(guild.id)] = "pl_PL"
            with open("vault.json", "w") as f:
                json.dump(data, f, indent=4)

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     self.vault = load_data()
    #     if not str(member.id) in self.vault["Economy"][str(member.guild)]:
    #         add_user(serverID=member.guild, userID=member.id)
    #         self.vault = load_data()

    # Commands

    @has_permissions(administrator=True)
    @commands.command(name="setvault", pass_context=True)
    async def set_vault(self, ctx, amount, mode):
        user = ctx.message.author.id
        user_name = ctx.message.author
        server = ctx.message.guild.id
        dictionary = lang.get(guild_lang(server))
        write_data(new_data=int(amount), serverID=str(server), userID=str(user), mode=str(mode))
        await ctx.send(f"{dictionary['set_vault_to']['1']} {user_name} {dictionary['set_vault_to']['2']} "
                       f"{amount} {dictionary['set_vault_to']['3']} {dictionary['set_vault_to'][str(mode.title())]}")

    @set_vault.error
    async def set_vault_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    @has_permissions(administrator=True)
    @commands.command(name="addvault", pass_context=True)
    async def add_vault(self, ctx, amount, mode):
        user = ctx.message.author.id
        server = ctx.message.guild.id
        dictionary = lang.get(guild_lang(server))
        add_data(amount=int(amount), serverID=str(server), userID=str(user), mode=str(mode))
        await ctx.send(f"{dictionary['add_vault']['1']} {user}\n"
                       f"{amount} {dictionary['add_vault']['2']} {dictionary['add_vault'][str(mode.title())]}")

    @add_vault.error
    async def add_vault_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    @has_permissions(administrator=True)
    @commands.command(name="subvault", pass_context=True)
    async def sub_vault(self, ctx, amount, mode):
        user = ctx.message.author.id
        server = ctx.message.guild.id
        dictionary = lang.get(guild_lang(server))
        subtract_data(userID=user, serverID=server, mode=mode, amount=amount)
        await ctx.send(f"{dictionary['sub_vault']['1']} {user}\n"
                       f"{amount} {dictionary['sub_vault']['2']} {dictionary['sub_vault'][str(mode.title())]}")

    @sub_vault.error
    async def sub_vault_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    @commands.command(name="balance", pass_context=True)
    async def balance(self, ctx):
        user = ctx.message.author.id
        server = ctx.message.guild.id
        dictionary = lang.get(guild_lang(server))
        self.vault = load_data()
        if not str(user) in self.vault["Economy"][str(server)]:
            add_user(serverID=server, userID=user)
            self.vault = load_data()
        vault_bank = self.vault["Economy"][str(server)][str(user)]["Bank"]
        vault_wallet = self.vault["Economy"][str(server)][str(user)]["Wallet"]
        await ctx.send(f"`{dictionary['balance']['user']} {user}\n"
                       f"{dictionary['balance']['guild']} {server}\n"
                       f"{dictionary['balance']['bank']} {vault_bank}\n"
                       f"{dictionary['balance']['wallet']} {vault_wallet}`")

    @balance.error
    async def balance_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    @commands.command(name="deposit", pass_context=True)
    async def deposit(self, ctx, amount=0):
        user = ctx.message.author.id
        server = ctx.message.guild.id
        dictionary = lang.get(guild_lang(server))
        self.vault = load_data()
        if not str(user) in self.vault["Economy"][str(server)]:
            add_user(serverID=server, userID=user)
            self.vault = load_data()
        if amount is 0:
            amount = self.vault["Economy"][str(server)][str(user)]["Wallet"]
            self.vault = load_data()
        if amount < 0:
            await ctx.send(f"{dictionary['errors']['negative_value']}")
            return
        if int(self.vault["Economy"][str(server)][str(user)]["Wallet"]) is 0:
            await ctx.send(f"{dictionary['errors']['not_enough_money']}")
            return
        if int(self.vault["Economy"][str(server)][str(user)]["Wallet"]) < amount:
            await ctx.send(f"{dictionary['errors']['invalid_money_too_much']}")
            return

        add_data(userID=user, serverID=server, mode="Bank", amount=amount)
        subtract_data(userID=user, serverID=server, mode="Wallet", amount=amount)
        await ctx.send(f"{dictionary['deposit']['1']} {amount} {dictionary['deposit']['2']}")

    @deposit.error
    async def deposit_error(self, ctx, error):
        await ctx.send(f"`{error}`")

    @commands.command(name="withdraw", pass_context=True)
    async def withdraw(self, ctx, amount=0):
        user = ctx.message.author.id
        server = ctx.message.guild.id
        dictionary = lang.get(guild_lang(server))
        self.vault = load_data()
        if not str(user) in self.vault["Economy"][str(server)]:
            add_user(serverID=server, userID=user)
            self.vault = load_data()
        if amount is 0:
            amount = self.vault["Economy"][str(server)][str(user)]["Bank"]
            self.vault = load_data()
        if amount < 0:
            await ctx.send(f"{dictionary['errors']['negative_value']}")
            return
        if int(self.vault["Economy"][str(server)][str(user)]["Bank"]) is 0:
            await ctx.send(f"{dictionary['errors']['not_enough_money']}")
            return
        if int(self.vault["Economy"][str(server)][str(user)]["Bank"]) < amount:
            await ctx.send(f"{dictionary['errors']['invalid_money_too_much']}")
            return

        add_data(userID=user, serverID=server, mode="Wallet", amount=amount)
        subtract_data(userID=user, serverID=server, mode="Bank", amount=amount)
        await ctx.send(f"{dictionary['withdraw']['1']} {amount} {dictionary['withdraw']['2']}")


def setup(client):
    client.add_cog(Vault(client))
