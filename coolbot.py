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

    await bot.change_presence(activity=discord.Game(name='with dy >_<'))
    print('e - nightclub BOT has started working!')

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
    if(message.content == "!welcome" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="**༚ ✧˳⁺ __Welcome to e- nightclub__  ⁺˳✧ ༚**", description="- We are so glad to have you join our server! By joining this server you agreed on our rules. \r\n\r\n - We have over 170+ roles, channels and some bots to play different games and much more! \r\n\r\n - Our channels are not aggressively moderated so feel free to join any conversation you like.", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    if(message.content == "!vcrules" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="**༚ ✧˳⁺ __Voice Chat rules__ ⁺˳✧ ༚**", description="__``1``__ • Don't ear rape other people with music or with your mic. \r\n\r\n __``2``__ • Do not spam music, let other people play their song. \r\n\r\n __``3``__ • Do not stop the music if there are still others in the voice channel. \r\n\r\n __``4``__ • Do not mic spam, yell or disturb others. \r\n\r\n __``5``__ • Do NOT be toxic or be racist.", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    if(message.content == "!rules" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="**༚ ✧˳⁺ __Server rules__ ⁺˳✧ ༚**", description="__``1``__ • Make sure to Follow **Discord TOS** and **Community Guidelines** (TOS:  ``https://discordapp.com/terms`` | Community Guidelines: ``https://discordapp.com/guidelines``). \r\n\r\n __``2``__ • Keep content in the appropriate channels. This includes only posting NSFW content in NSFW marked channels. \r\n\r\n __``3``__ • No Doxing / Do not leak someone's IP address / Do not share personal information of anyone. \r\n\r\n __``4``__ • Any type of serious harassment [Blackmailing, Hate speech, DM spamming members, etc..]. Will result in a ban. \r\n\r\n __``5``__ • No advertising (Including PM advertisement). \r\n\r\n __``6``__ • Do NOT tell people to kill themselves (even if it's a joke). \r\n\r\n __``7``__ • Do not impersonate other users. Impersonating our staff team or discord staff will result in a permanent ban. \r\n\r\n __``8``__ • Remember that this server is English only! Try to avoid using any other languages so everyone can understand each other and have fun. \r\n\r\n __``9``__ • Respect all staff and follow their instructions. Especially the owners ( dy & scopes ). \r\n\r\n __``10``__ • Do NOT set people up against each other or against STAFF. \r\n\r\n __``11``__ • Respect people's wishes considering revealing their age, face reveal etc. \r\n\r\n __``12``__ • Asking for nudes or for other information is ABSOLUTELY not accepted here and will result in a ban. \r\n\r\n **- Please contact <@495680416422821888> if you have any issues with Staff or the rules posted above.** \r\n\r\n **- Make sure to check <#567371465633169436> if you're new to discord or have any questions.** \r\n\r\n **- Thank you for joining e- nightclub! We hope you have a great stay here!**", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    # shiki command


# put mention cmd here.


# BOT LOGIN
bot.run("TOKEN")
