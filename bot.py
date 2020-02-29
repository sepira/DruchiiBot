# bot.py

import os

import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')


@bot.command(name='attendance', help='Pass voice channel as an argument')
async def attendance(ctx, channel):
    member_count = 0
    guild = ctx.guild
    voice_channel = discord.utils.get(guild.channels, name=channel, type=discord.ChannelType.voice)

    if not voice_channel.members:
        await ctx.send('No members inside this voice chat!')
    else:
        for member in voice_channel.members:
            member_count += 1
        await ctx.send(f'This is the list of Druchii members who attended VC on {datetime.date.today()} : \n')
        await ctx.send("\n".join([member.display_name for member in voice_channel.members]))
        await ctx.send(f'Member count: {member_count}')

@attendance.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that channel...')

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Pass a voice chat channel to check attendance! ')

bot.run(TOKEN)
