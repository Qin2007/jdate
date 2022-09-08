from math import floor

import disnake
from disnake.ext import commands

intents = disnake.Intents(guilds=True)
ibot = commands.InteractionBot(intents=intents)


@ibot.slash_command(description='member created?')
async def memberjoin(inter, member: disnake.Member):
    cta = floor(member.created_at.timestamp())

    ja_ = floor(member.joined_at.timestamp())
    await inter.send(f'time created <t:{cta}:R> that is <t:{cta}:D>\ntime joined <t:{ja_}:R> that is <t:{ja_}:D>\n')


@ibot.user_command(name='created?')
async def memberj(inter, member: disnake.Member):
    cta = floor(member.created_at.timestamp())

    ja_ = floor(member.joined_at.timestamp())
    await inter.send(f'time created <t:{cta}:R> that is <t:{cta}:D>\ntime joined <t:{ja_}:R> that is <t:{ja_}:D>\n')


@ibot.slash_command(description='server created?')
async def guildcreated(inter):
    guild: disnake.Guild = inter.guild
    gca = floor(guild.created_at.timestamp())
    await inter.send(f'time created <t:{gca}:R> that is <t:{gca}:D>')


@ibot.slash_command(description='role created?')
async def rolecreated(inter, role: disnake.Role):
    createdat = floor(role.created_at.timestamp())
    await inter.send(f'time created <t:{createdat}:R> that is <t:{createdat}:D>')


@ibot.slash_command(description='channel created?')
async def channelcreated(inter, channel: disnake.abc.GuildChannel):
    createdat = floor(channel.created_at.timestamp())
    await inter.send(f'time created <t:{createdat}:R> that is <t:{createdat}:D>')


@ibot.slash_command(description='message created?')
async def messagecreated(inter, mgs: disnake.Message):
    createdat = floor(mgs.created_at.timestamp())
    await inter.send(f'time created <t:{createdat}:R> that is <t:{createdat}:D>')


@ibot.message_command(name='created?')
async def messagec(inter, mgs: disnake.Message):
    createdat = floor(mgs.created_at.timestamp())
    await inter.send(f'time created <t:{createdat}:R> that is <t:{createdat}:D>')


ibot.run(input('created the token?'))
