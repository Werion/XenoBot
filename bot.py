import random
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle
import json
import os


# prefixes = '.'

# prefix = prefixes

# Load Config

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


def create_config():
    # prefixes.json file exist check
    if not os.path.exists('prefixes.json'):
        (
            open("prefixes.json", 'a', encoding='utf-8').close(),
            print("Prefixes.json created")
        )


# prefix = '!!!'


client = commands.Bot(command_prefix=get_prefix)
status = cycle(['Wersja 0.0.4'])


# status = f"{round(client.latency * 1000)}ms"


@client.event
async def on_ready():
    change_status.start()
    print("Status: OK")
    print("Bot ready!")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    # user = client.get_user(member)
    print(f'{member} joined 4FUN.')
    # await user.send(f'Witaj {member} na serwerze Meweria. Jestem autorskim botem który posłurzy gdybyś miał jakiś problem.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left 4FUN.')


@client.command()
async def ping(ctx):
    await ctx.send(f'`{round(client.latency * 1000)}ms`')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'To pewne.',
        'Tak jest zdecydowanie.',
        'Bez wątpienia.',
        'Tak - napewno',
        'Możesz na tym polegać.',
        'Tak, jak widzę, tak.',
        'Najprawdopodobniej.',
        # 'Outlook good.',
        'Tak.',
        'Znaki wskazują na tak.',
        'Odpowiedź mglista, spróbuj ponownie.',
        'Zapytaj ponownie później.',
        'Lepiej ci teraz nie mówić.',
        'Nie można teraz przewidzieć.',
        'Skoncentruj się i zapytaj ponownie.',
        "Nie licz na to.",
        'Moja odpowiedź brzmi nie.',
        'Moje źródła mówią nie.',
        'Perspektywa niezbyt dobra.',
        'Bardzo wątpliwe.',

    ]
    # await ctx.send(f"{ctx.message.author}\nPytanie: {question}\nOdpowiedź: {random.choice(responses)}")
    await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('Panie, pan nie ma uprawnień by użyć tej komendy!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'`Użycie: 8ball' + ' [pytanie]`')


@client.command(name="clear", pass_context=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Błąd", description="Nieprawidłowy syntax")
        embed.add_field(name="Użycie:", value=f"clear [ilość]", inline=False)
        await ctx.send(embed=embed)


@client.command(name="kick", pass_context=True)
@has_permissions(kick_members=True)
async def _kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'`Kicked {member.mention}`')


@_kick.error
async def kick_error(ctx, error, prefix):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Błąd", description="Nieprawidłowy syntax")
        embed.add_field(name="Użycie:", value=f"kick [nazwa]" " {powód}", inline=False)
        await ctx.send(embed=embed)


@client.command(name="ban", pass_context=True)
@has_permissions(ban_members=True)
async def _ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason, )
    await ctx.send(f'`Banned {member.mention}`')


@_ban.error
async def ban_error(ctx, error, prefix):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'`Użycie: ban' + ' [Użyytkownik] {Powód}`')


@client.command(name="unban", pass_context=True)
async def _unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'`Unbanned {user.mention}`')
            return


@_unban.error
async def unban_error(error, ctx):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('`Panie, pan nie ma uprawnień by użyć tej komendy!`')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('`Użycie: unban [Użyytkownik] {Powód}`')


@client.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="Werion Bot", description="description")
    embed.set_author(name="Werion", )
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/646398082845769759/886b06c4dee4c4d487493c83a79751a3.png")
    embed.add_field(name="Test", value="1234", inline=False)
    embed.set_footer(text="version 0.0.4")
    await ctx.send(embed=embed)

    # await client.send_message(channel, embed=embed)


@client.command(name="dm", pass_context=True)
async def _dm(ctx, *, question):
    user = client.get_user(240117268745289729)
    await user.send(f'{ctx.author.mention}: {question}')
    await ctx.send(f'`Wysłano pytanie do {user}: {question}`')


@client.command(name="jd", pass_context=True)
async def _jd(ctx):
    await ctx.send(f'JD')


@client.command(name="staff_dm", pass_context=True)
@has_permissions(administrator=True)
async def _staff_dm(ctx, id=int(), *, question):
    user = client.get_user(id)
    await user.send(f'{ctx.author.mention}: {question}')
    await ctx.send(f'`Wysłano pytanie do {user}: {question}`')


@_staff_dm.error
async def _staff_dm_error(ctx, error):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('Panie, pan nie ma uprawnień by użyć tej komendy!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'`Użycie: staff_dm' + ' [ID Uzytkownika Discord] [Tekst]`')


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Zmieniono prefix na {prefix}')


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


if __name__ == '__main__':
    create_config()
    client.run('')