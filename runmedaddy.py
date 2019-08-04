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
    if(bot.guild.id == 448571905524498432):
        channel = discord.utils.get(server.channels, name="☆│lounge") 
        await channel.send("Welcome {} to **e nightclub!** You’re the {}.".format(member.mention, server.member_count))

@bot.event
async def on_member_remove(member):
    if(member.guild.id == 448571905524498432):
        channel = discord.utils.get(server.channels, name="✵│arrivals")
        await channel.send("**{}** has left the server. We now have **{}** members.".format(member.mention, member.guild.member_count))

bot.run(os.environ.get("token"))
