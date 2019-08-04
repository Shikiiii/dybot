import discord
from discord import Message, Guild
from discord.ext.commands import Bot
from typing import Optional, Set

bot = Bot(command_prefix='!')
bot.remove_command('help')

server: Optional[Guild] = None

@bot.event
async def on_ready():
    global server
    server = bot.get_guild(448571905524498432)

    await bot.change_presence(activity=discord.Game(name='with your feelings.'))
    print('Ready!')

@bot.event
async def on_member_join(member):
    if(member.guild.id == 448571905524498432):
        channel = discord.utils.get(member.guild.channels, name="☆│lounge")
        channel2 = discord.utils.get(member.guild.channels, name="✵│welcome-rules")
        channel3 = discord.utils.get(member.guild.channels, name="∞│roles-menu")
        channel4 = discord.utils.get(member.guild.channels, name="✵│faq")
        await channel.send("Welcome {} to **e nightclub!** You’re the **{}** member. \n\n Make sure to read: {}  |  Roles: {}  |  For help:  {}.".format(member.mention, member.guild.member_count, channel2.mention, channel3.mention, channel4.mention))

@bot.event
async def on_member_remove(member):
    if(member.guild.id == 448571905524498432):
        channel = discord.utils.get(member.guild.channels, name="✵│arrivals")
        await channel.send("**{}** has left the server. We now have **{}** members.".format(member.mention, member.guild.member_count))

bot.run(os.environ.get("token"))
