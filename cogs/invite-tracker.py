import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import DiscordUtils


class InvTracker(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.tracker = DiscordUtils.InviteTracker(client)

    # Events
 #   @commands.Cog.listener()
 #   async def on_ready(self):
#       print("> Invite Tracking module: Ready")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.tracker.cache_invites()

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        await self.tracker.update_invite_cache(invite)
        print(f"Invite created {invite}")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.tracker.update_guild_cache(guild)
        print(f"At: {guild}")

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        await self.tracker.remove_invite_cache(invite)
        print(f"Invite removed {invite}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.tracker.remove_guild_cache(guild)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        inviter = await self.tracker.fetch_inviter(member)  # inviter is the member who invited
        data = await self.client.invites.find(inviter.id)
        if data is None:
            data = {"_id": inviter.id, "count": 0, "userInvited": []}
            print(f"data created")

        data["count"] += 1
        data["usersInvited"].append(member.id)
        await self.client.invites.upsert(data)

        channel = discord.utils.get(member.guild.text_channels, name="rec")
        embed = discord.Embed(
            title=f"Welcome {member.display_name}",
            description=f"Invited by: {inviter.mention}\nInvites: {data['count']}",
            timestamp=member.joined_at
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(InvTracker(client))
