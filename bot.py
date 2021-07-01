from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
import os
from dotenv import load_dotenv


# Load Config

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(
    command_prefix=get_prefix,
    owner_id=os.getenv('BOT_OWNER')
)
client.version = "1.0.2"
# client.remove_command('help')

# Cogs loading/unloading --------------------------------------


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'`Loaded: {extension}`')


@load.error
async def load_error(ctx, error):
    if isinstance(error, MissingPermissions):
        # text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send('Panie, pan nie ma uprawnień by użyć tej komendy!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'`Użycie: load' + ' [nazwa modułu]`')
    await ctx.send(f'`{error}`')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'`Unloaded: {extension}`')


@unload.error
async def unload_error(ctx, error):
    await ctx.send(f'`{error}`')


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'`Reloaded: {extension}`')


@reload.error
async def reload_error(ctx, error):
    await ctx.send(f'`{error}`')


# Load every cog from ./cogs dir

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith("_"):
        client.load_extension(f'cogs.{filename[:-3]}')


# -------------------------------------------------------------

@client.event
async def on_ready():
    print("")
    print("> Main Component: Ready")
    print("------------------------")
    print("")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'`Nie poznaje tej komędy!`')
        print(error)
    else:
        print(f'Error was found !!! \n'
              f'{error}')




# @client.event
# async def on_member_join(member):
# user = client.get_user(member)
# print(f'{member} joined')
# await user.send(f'Witaj {member} na serwerze Meweria. Jestem autorskim botem który posłurzy gdybyś miał jakiś
# problem.')


# @client.event
# async def on_member_remove(member):
#    print(f'{member} has left')


# | Guild prefix add/remove | START ---------------------------------------

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


# END ---------------------------------------------------------------------
# | Change prefix | START -------------------------------------------------
@client.command()
@has_permissions(administrator=True)
async def change_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Zmieniono prefix na {prefix}')


# | Create prefix.json if there is none | START ----------------------------
def path_exist_check():
    if not os.path.exists('prefixes.json'):
        data = {}
        with open('prefixes.json', 'w') as outfile:
            json.dump(data, outfile)


# END ----------------------------------------------------------------------
# | Disable certain command on certain server (guild) | START --------------
commandsEnabled = {}


@client.event
async def on_guild_join(guild):
    commandsEnabled[str(guild.id)] = {}
    for cmd in client.commands:
        commandsEnabled[str(guild.id)][cmd.name] = True


# @client.command()
# @has_permissions(administrator=True)
# async def toggle(ctx, command):
#    commandsEnabled[str(guild.id)][cmd.name] = not commandsEnabled[str(guild.id)][cmd.name]
#    await ctx.send(f"{command} command {['disabled', 'enabled'][int()]}")


# @toggle.error
# async def about_error(ctx, error):
#    await ctx.send(f'`{error}`')


# MAIN ---------------------------------------------------------------------

if __name__ == '__main__':
    print("Loading, please wait...")
    load_dotenv()
    path_exist_check()
    client.run(os.getenv('BOT_TOKEN'))
