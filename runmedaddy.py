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

@bot.event
async def on_message(message: Message):
    if(message.content == "!rules" and (message.author.id == 393839495859929089 or 495680416422821888)):
        embed = discord.Embed(title="cool title", description="cool description", color=0xFF93F0)
        embed.set_image(url="link goes here")
        await message.channel.send(embed=embed)
    elif(message.content == "!faq" and (message.author.id == 393839495859929089 or 495680416422821888)):
        embed = discord.Embed(title="cool title", description="cool description", color=0xFF93F0)
        embed.set_image(url="link goes here")
        await message.channel.send(embed=embed)
    elif(message.content == "!vcrules" and (message.author.id == 393839495859929089 or 495680416422821888)):
        embed = discord.Embed(title="cool title", description="cool description", color=0xFF93F0)
        embed.set_image(url="link goes here")
        await message.channel.send(embed=embed)

bot.run(os.environ.get("token"))
