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
    if(message.content == "!faq" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="*__**FAQ**:__*", description="__**How can I level up?**__ \r\n\r\n To level up you have to be active in any channel in the server, avoid spamming. Spamming won't level you up. \r\n\r\n __**Is there a way to get picture perms/embed links?**__ \r\n\r\n Yes there is a way to get these perms, when you reach **level 10+** you'll be able to post pictures or links in <#491366183447298068>. \r\n\r\n __**Someone is advertising in my DMS what do I do?**__ \r\n\r\n Dm a staff member and they'll ban them as soon as possible. \r\n\r\n __**Staff is abusing his perms, what do I do?**__ \r\n\r\n Dm <@303564745565536256> or <@495680416422821888>. \r\n\r\n __**Is there a NSFW channel?**__ \r\n\r\n Yes there is, to get access to the NSFW + shitpost channels you have to get the NSFW role. (can be found in <#491368164370677781>). \r\n\r\n __**Do you guys do giveaways and events?**__ \r\n\r\n Yes we do events and giveaways sometimes. (get the events + giveaway roles in <#491368164370677781> so you don't miss our giveaways and events!) \r\n\r\n __**I want to become a Staff member for e - nightclub , how can I apply?**__ \r\n\r\n You can apply in <#566420979069222912> by typing **!apply** there! Please do not annoy the owners to get Mod/Admin. \r\n\r\n __**I want to apply for a Partner Manager, how can I do that?**__ \r\n\r\n Dm dy#0777. \r\n\r\n __**Where can I shoutout my instagram , snapchat, etc..?**__ \r\n\r\n You can send your snapcode in <#558992750612054036>, for instagram go to <#558992817532436521>.", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    if(message.content == "!faq2" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="", description="__**Can we be partners?**__ \r\n\r\n Sure! You can be partner with us by messaging dy#0777 or a Partner Manager. \r\n\r\n __**What can I do with the bot money?**__ \r\n\r\n You can bet, buy items, gamble and much more. \r\n\r\n __**How can I get access to <#558991846785679360> & <#558992153393496074> ?**__ \r\n\r\n To get access to one of these channels please make sure to read <#558991108915462164>. However we've got a channel without verification (can be found here <#558992392242331658>.) \r\n\r\n __**How can I play a song in music voice chat?**__ \r\n\r\n Go to <#559063589114216470> and type ``$play [song name or URL]`` │You can also use ``%play [song name or URL]``. \r\n\r\n __**I got banned for no reason, what do I do?**__ \r\n\r\n Simply DM one of the owners **dy#0777 or scopes#9333** and we'll unban you as soon as possible! \r\n\r\n __**Can I get a color?**__ \r\n\r\n Yes, you can pick a color form our colors menu. (check them here <#566212667837120522>). \r\n\r\n __**Someone leaked my pictures, IP, phone number. What do I do?**__ \r\n\r\n DM one of the Staff members and they'll ban them. \r\n\r\n __**Where can I find the server's leaderboard for levels?**__ \r\n\r\n You can find it here: https://mee6.xyz/leaderboard/448571905524498432 \r\n\r\n __**When was this server created?**__ \r\n\r\n created on 22 May 2018. \r\n\r\n __**Is this a dating server?**__ \r\n\r\n Nope, this is a chill server to talk to new people and make friends. However we're not going to do anything if you date here. This is not our business.", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    if(message.content == "!staff" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="**__Staff Members:__**", description="☆ - Owners: dy <@495680416422821888> | scopes <@303564745565536256>. \r\n\r\n ☆ - Co Owners: Blitzzy <@322362178306965504> | Djimi <@322361798625853441> | Ave <@340478577906548737> | Ashton <@335445790808080385> | Blury <@315076865171783682> \r\n\r\n ☆ - Head Admins: N/A \r\n\r\n ☆ - Admins: Quenty <@243218955014111232> | Lil Akame <@464447422249304084> \r\n\r\n ☆ - Mods: Poppy <@454036738885681162> | Sammy <@541048817307353095>", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    if(message.content == "!invites" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed = discord.Embed(title="**__Perm invite links:__**", description="🔗 Perm invite link: https://discord.gg/UrbUgWH \r\n\r\n 🔗 You can also use this link: https://invite.gg/enightclub \r\n\r\n Last updated: 07/23/2019", color=0xFF93F0)
        embed.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        await message.channel.send(embed=embed)
    # shiki command


# put mention cmd here.


# BOT LOGIN
bot.run("NTkzMDkwMjU2NTYwMTkzNTQ5.XUdAXQ._lBNotPUrC6klxCGWCT7QhJwhGs")
