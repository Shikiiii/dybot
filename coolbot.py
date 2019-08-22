# a discord custom bot made by shiki & dy for e - nightclub server.

# 08/03/2019 | 2020-2019

# (c) MIT License @ Shiki

import discord
from discord import Message, Guild, Member
from discord.ext.commands import Bot
from typing import Optional, Set
from discord.ext import commands

import sys
import traceback
import asyncio
from datetime import datetime
import datetime
import random
import http.client
import json
import requests

bot = Bot(command_prefix='!')
bot.remove_command('help')

server: Optional[Guild] = None

shiki: Optional[Member] = None

# bot status.

@bot.event
async def on_ready():
    global server
    server = bot.get_guild(448571905524498432)

    global shiki
    shiki = server.get_member(393839495859929089)

    await bot.change_presence(activity=discord.Game(name='!'))
    print('e - nightclub BOT has started working!')

    await bot.wait_until_ready()
    guildd = bot.get_guild(448571905524498432)
    #print("+++++++++++++++ \n" + str(guildd) + "+++++++++++++++++++")

    while True:
        channel = discord.utils.get(guildd.channels, name="☆│lounge")
        apply = discord.utils.get(guildd.channels, name="✵│apply-for-staff")
        embed2 = discord.Embed(title="Reminder:", description="You can bump the server by typing **!d bump** and help our server grow.", color=0xffffff)
        embed2.set_thumbnail(url=guildd.icon_url)
        embed1 = discord.Embed(title="Reminder:", description="Check out <#558991108915462164> to get verified role.", color=0xffffff)
        embed1.set_thumbnail(url=guildd.icon_url)
        embed3 = discord.Embed(title="Reminder:", description="If you want to apply for **Partnership Mananger** or **Server Helper**, type **!!apply** in {}.".format(apply), color=0xffffff)
        embed3.set_thumbnail(url=guildd.icon_url)
        #try:
        await channel.send(embed=embed2)
        #except:
        #print("oh okay that broke")
        await asyncio.sleep(float(7200))
        #try:
        await channel.send(embed=embed1)
        #except:
        #print("oh okay, that broke 2")
        await asyncio.sleep(float(7200))
        #try:
        await channel.send(embed=embed3)
        #except:
        #print("oh okay that broke")
        await asyncio.sleep(float(7200))

# welcome message

@bot.event
async def on_member_join(member):
    if(member.guild.id == 448571905524498432):
        mbrcnt = discord.get_channel(613577536584286218)
	await mbrcnt.edit(name="Server Members: {}".format(member.guild.member_count))
        channel = discord.utils.get(member.guild.channels, name="☆│lounge")
        channel2 = discord.utils.get(member.guild.channels, name="✵│welcome-rules")
        channel3 = discord.utils.get(member.guild.channels, name="∞│roles-menu")
        channel4 = discord.utils.get(member.guild.channels, name="✵│faq")
        embed = discord.Embed(description="Welcome to **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**! You're the **{}th** member. \n\n Make sure to read: {}  \n\nRoles: {}  \n\nFor help:  {}.".format(member.guild.member_count, channel2.mention, channel3.mention, channel4.mention), color=0x000000)
        embed.set_author(name="{}".format(member), icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.guild.icon_url)
        await channel.send("{}".format(member.mention))
        await channel.send(embed=embed)
        channel = discord.utils.get(member.guild.channels, name="✵│arrivals")
        await channel.send("Welcome to **e- nightclub**, **{}** has joined the server. We now have **{}** members.".format(member.mention, member.guild.member_count))
        #await channel.send("Welcome {} to **e nightclub!** You’re the **{}** member. \n\n Make sure to read: {}  |  Roles: {}  |  For help:  {}.".format(member.mention, member.guild.member_count, channel2.mention, channel3.mention, channel4.mention))
        chan = discord.utils.get(member.guild.channels, name="∞│roles-menu")
        msg = await chan.send(f"Hi! {member.mention}, Check out our roles!")
        await asyncio.sleep(60)
        msg.delete()


# leave message & join message.

@bot.event
async def on_member_remove(member):
    if(member.guild.id == 448571905524498432):
        mbrcnt = discord.get_channel(613577536584286218)
	await mbrcnt.edit(name="Server Members: {}".format(member.guild.member_count))
        channel = discord.utils.get(member.guild.channels, name="✵│left")
        await channel.send("**{}** has left the server. We now have **{}** members.".format(member.mention, member.guild.member_count))

# EMBED MESSAGES

@bot.event
async def on_message(message: Message):
    if message.guild.id == 448571905524498432 and message.channel.id == 613792979039158274:
        chan = discord.utils.get(message.guild.channels, name="☆│lounge")
        await chan.send("{}".format(message.content))
    if len(message.mentions) > 0:
        if message.author.id != 593090256560193549:
            for key in afklist:
                usr = message.guild.get_member(key)
                if usr.mentioned_in(message):
                    reason = afklist[key]
                    await message.channel.send("{} is AFK: **{}**".format(usr.mention, str(reason)))
    if message.author.id in afklist:
        del afklist[message.author.id]
        await message.channel.send("Welcome back, {}! I removed your AFK.".format(message.author.mention))
    if(message.content == "!welcome" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Welcome to e- nightclub__  ⁺˳✧ ༚**", description="- We are so glad to have you join our server! By joining this server you agreed on our rules. \r\n\r\n - We have over 170+ roles, channels and some bots to play different games and much more! \r\n\r\n - Our channels are not aggressively moderated so feel free to join any conversation you like.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/j6HHIdWsJFuPTPfNlW/giphy.gif")
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
    elif(message.content == "!rules" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Server rules__ ⁺˳✧ ༚**", description="__``1``__ • Make sure to Follow **Discord TOS** and **Community Guidelines** (TOS:  ``https://discordapp.com/terms`` | Community Guidelines: ``https://discordapp.com/guidelines``). \r\n\r\n __``2``__ • Keep content in the appropriate channels. This includes only posting NSFW content in NSFW marked channels. \r\n\r\n __``3``__ • No Doxing / Do not leak someone's IP address / Do not share personal information of anyone. \r\n\r\n __``4``__ • Any type of serious harassment [Blackmailing, Hate speech, DM spamming members, etc..]. Will result in a ban. \r\n\r\n __``5``__ • No advertising (Including PM advertisement). \r\n\r\n __``6``__ • Do NOT tell people to kill themselves (even if it's a joke). \r\n\r\n __``7``__ • Do not impersonate other users. Impersonating our staff team or discord staff will result in a permanent ban. \r\n\r\n __``8``__ • Remember that this server is English only! Try to avoid using any other languages so everyone can understand each other and have fun. \r\n\r\n __``9``__ • Respect all staff and follow their instructions. Especially the owners ( dy & scopes ). \r\n\r\n __``10``__ • Do NOT set people up against each other or against STAFF. \r\n\r\n __``11``__ • Respect people's wishes considering revealing their age, face reveal etc. \r\n\r\n __``12``__ • Asking for nudes or for other information is ABSOLUTELY not accepted here and will result in a ban. \r\n\r\n **- Please contact <@495680416422821888> if you have any issues with Staff or the rules posted above.** \r\n\r\n **- Make sure to check <#567371465633169436> if you're new to discord or have any questions.** \r\n\r\n **- Thank you for joining e- nightclub! We hope you have a great stay here!**", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        embed3 = discord.Embed(title="**༚ ✧˳⁺ __Voice Chat rules__ ⁺˳✧ ༚**", description="__``1``__ • Don't ear rape other people with music or with your mic. \r\n\r\n __``2``__ • Do not spam music, let other people play their song. \r\n\r\n __``3``__ • Do not stop the music if there are still others in the voice channel. \r\n\r\n __``4``__ • Do not mic spam, yell or disturb others. \r\n\r\n __``5``__ • Do NOT be toxic or be racist.", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed1)
    elif(message.content == "!faq" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="*__**FAQ**:__*", description="__**How can I level up?**__ \r\n\r\n To level up you have to be active in any channel in the server, avoid spamming. Spamming won't level you up. \r\n\r\n __**Is there a way to get picture perms/embed links?**__ \r\n\r\n Yes there is a way to get these perms, when you reach **level 10+** you'll be able to post pictures or links in <#491366183447298068>. \r\n\r\n __**Someone is advertising in my DMS what do I do?**__ \r\n\r\n Dm a staff member and they'll ban them as soon as possible. \r\n\r\n __**Staff is abusing his perms, what do I do?**__ \r\n\r\n Dm <@303564745565536256> or <@495680416422821888>. \r\n\r\n __**Is there a NSFW channel?**__ \r\n\r\n Yes there is, to get access to the NSFW + shitpost channels you have to get the NSFW role. (can be found in <#491368164370677781>). \r\n\r\n __**Do you guys do giveaways and events?**__ \r\n\r\n Yes we do events and giveaways sometimes. (get the events + giveaway roles in <#491368164370677781> so you don't miss our giveaways and events!) \r\n\r\n __**I want to become a Staff member for e - nightclub , how can I apply?**__ \r\n\r\n You can apply in <#566420979069222912> by typing **!apply** there! Please do not annoy the owners to get Mod/Admin. \r\n\r\n __**I want to apply for a Partner Manager, how can I do that?**__ \r\n\r\n Dm dy#0777. \r\n\r\n __**Where can I shoutout my instagram , snapchat, etc..?**__ \r\n\r\n You can send your snapcode in <#558992750612054036>, for instagram go to <#558992817532436521>.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/kH73TzZ51Lz0ocgRJR/giphy.gif")
        embed3 = discord.Embed(title="", description="__**Can we be partners?**__ \r\n\r\n Sure! You can be partner with us by messaging dy#0777 or a Partner Manager. \r\n\r\n __**What can I do with the bot money?**__ \r\n\r\n You can bet, buy items, gamble and much more. \r\n\r\n __**How can I get access to <#558991846785679360> & <#558992153393496074> ?**__ \r\n\r\n To get access to one of these channels please make sure to read <#558991108915462164>. However we've got a channel without verification (can be found here <#558992392242331658>.) \r\n\r\n __**How can I play a song in music voice chat?**__ \r\n\r\n Go to <#559063589114216470> and type ``$play [song name or URL]`` │You can also use ``%play [song name or URL]``. \r\n\r\n __**I got banned for no reason, what do I do?**__ \r\n\r\n Simply DM one of the owners **dy#0777 or scopes#9333** and we'll unban you as soon as possible! \r\n\r\n __**Can I get a color?**__ \r\n\r\n Yes, you can pick a color form our colors menu. (check them here <#566212667837120522>). \r\n\r\n __**Someone leaked my pictures, IP, phone number. What do I do?**__ \r\n\r\n DM one of the Staff members and they'll ban them. \r\n\r\n __**Where can I find the server's leaderboard for levels?**__ \r\n\r\n You can find it here: https://mee6.xyz/leaderboard/448571905524498432 \r\n\r\n __**When was this server created?**__ \r\n\r\n created on 22 May 2018. \r\n\r\n __**Is this a dating server?**__ \r\n\r\n Nope, this is a chill server to talk to new people and make friends. However we're not going to do anything if you date here. This is not our business.", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    elif(message.content == "!staff" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**__Staff Members:__**", description="☆ - Owners: dy <@495680416422821888> | scopes <@303564745565536256>. \r\n\r\n ☆ - Co Owners: Blitzzy <@322362178306965504> | Djimi <@322361798625853441> | Ave <@340478577906548737> | Ashton <@335445790808080385> | Blury <@315076865171783682> \r\n\r\n ☆ - Head Admins: N/A \r\n\r\n ☆ - Admins: Quenty <@243218955014111232> | Lil Akame <@464447422249304084> \r\n\r\n ☆ - Mods: Poppy <@454036738885681162> | Sammy <@541048817307353095>", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/Xy1debdAWrNLK3cnHk/giphy.gif")
        embed3 = discord.Embed(title="**__Perm invite links:__**", description="🔗 Perm invite link: https://discord.gg/UrbUgWH \r\n\r\n 🔗 You can also use this link: https://invite.gg/enightclub \r\n\r\n Last updated: 08/05   /2019", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    elif(message.content == "!verification" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ Verification ⁺˳✧ ༚**", description="✧ - Post selfie in <#558991375681716256> with 'e- Nightclub and your discord username' on a piece of paper to get verified! \r\n\r\n ✧ - Verified role gives you access to <#558992153393496074> or <#558991846785679360> depends on your gender. \r\n\r\n ✧ - **NOTE:** You cannot use a photo that you took for another server. \r\n\r\n You can also Dm me or dm a staff member to role you verified if you don't want to post your face in <#604506916051484683>.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)
    elif(message.content == "!verification" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ Verification ⁺˳✧ ༚**", description="✧ - Post selfie in <#558991375681716256> with 'e- Nightclub and your discord username' on a piece of paper to get verified! \r\n\r\n ✧ - Verified role gives you access to <#558992153393496074> or <#558991846785679360> depends on your gender. \r\n\r\n ✧ - **NOTE:** You cannot use a photo that you took for another server. \r\n\r\n You can also Dm me or dm a staff member to role you verified if you don't want to post your face in <#604506916051484683>.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)
    elif(message.content == "!verified" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="*New member is verified!", description="༚ ✧˳⁺ Member has recieived verified role. ⁺˳✧ ༚ ", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)
    elif(message.content == "!rewards" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="", description="**──────────» ✰║ Invite Rewards ║✰ «──────────** \r\n\r\n - | ``✰`` | - **__5__ invites:** Pic perms or Respected role (you can only pick one role.) \r\n\r\n - | ``✰`` | - **__10__ invites:** Custom role with color! (last 30 days.) \r\n\r\n - | ``✰`` | - **__20__ invites:** Custom role with private channel (can give anyone access to it.) \r\n\r\n - | ``✰`` | - **__50__ invites:** Classic nitro (5$). \r\n\r\n - | ``✰`` | - **__75__ invites:** Server promo with ping ``@everyone`` \r\n\r\n **─────────────» ✰║ Note: ║✰ «─────────────** \r\n\r\n **➜** Your level must be at least **5+** to get your prize. \r\n\r\n **➜** Make sure to make your **OWN** permanent instant invite. \r\n\r\n **➜** Do NOT make alts to join the server with your invite code. \r\n\r\n **➜** After receiving your prize we'll reset your invites back to **0**. \r\n\r\n **➜** Type **>invites** in <#559063589114216470> to check how many people you have invited. \r\n\r\n Dm <@495680416422821888> if you have any questions.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)
    elif message.content == "invite":
        online = 0
        for member in message.guild.members:
            if member.status != discord.Status.offline:
                online += 1
        embed = discord.Embed(description="\n[e - nightclub](https://invite.gg/enightclub) \n\n- Giveaways | Chill chat & make friends | socials and more! \n\n⬤ {} Online ⭘ {} Members".format(online, message.guild.member_count), color=0x000000)
        embed.set_author(name="YOU'VE BEEN INVITED TO JOIN A SERVER\n", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
        msg = await message.channel.send("Get the direct link DMed to you by reacting here!")
        await msg.add_reaction("📧")
        
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '📧'
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            try:
                await message.author.send("Direct link: https://invite.gg/enightclub", embed=embed)
            except:
                await message.channel.send("{}, your DMs are disabled, so I couldn't DM you the invite link!".format(ctx.message.author.mention))
            await msg.delete()
# dy  & shiki dms commands:

  #  if "xxx" in message.content:
     #   await message.author.send("Hi")
    #elif shiki in message.mentions:
        #await message.author.send(f"Hey there, {message.author.mention}! \nPlease don't abusively mention the Devs without a reason. If you want to just talk to them, it's okay, but don't don it oftenly without a real reason. But while you're here... \n\n Are you looking for **cheap** and sometimes **free** __bot developing and hosting__? Our **custom bot**, <@593090256560193549> was made by the user you just pinged, {shiki.mention}. \n\n If you're interesting in having a custom bot like this one, **DM {shiki.mention}** and we'll talk about it there. \n\n > This automatic action was fired because you pinged either the Bot Coder role or {shiki.mention}.")
    elif message.content == "dy":
        await message.channel.send("dy >_<")
    elif message.content == "lumen":
        await message.channel.send("LUMEN XD")
    elif message.content == "shiki":
        await message.channel.send(">.<")
    elif message.content == "!!apply":
        await message.channel.send("Thank you for applying! Please check your DMs to complete the application.")
    elif message.content == "no u" and message.author.id != 593090256560193549:
        await message.channel.send("no u")

    await bot.process_commands(message)

tosnipe = {}
tosnipeauthors = {}
tosnipetime = {}
			
@bot.event
async def on_message_delete(message: Message):
	if message.author.bot == False:
		logch = discord.utils.get(message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Deleted a message in {}: \n{}\n\nUsers ID: {}".format(message.channel.mention, message.content, message.author.id), color=0xFFFFFF)
		log.set_author(name="{}".format(message.author), icon_url=message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=message.author.avatar_url)
		await logch.send(embed=log)

	if message.author.bot == False:
		tosnipe[message.channel.id] = message.content
		tosnipeauthors[message.channel.id] = message.author
		timestamp2 = datetime.datetime.now()
		corfor = timestamp2.strftime("%d %b, %Y at %H:%M")
		tosnipetime[message.channel.id] = timestamp2
		

toeditsnipe = {}
toeditsnipeauthors = {}
toeditsnipetime = {}
	
@bot.event
async def on_message_edit(before, after):
	if before.author.bot == False:
		#print(before)
		#print(after)
		logch = discord.utils.get(before.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Edited a message in {}: \n``Old:``\n{}\n``New:``\n{}\n\nUsers ID: {}".format(before.channel.mention, before.content, after.content, before.author.id), color=0xFFFFFF)
		log.set_author(name="{}".format(before.author), icon_url=before.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=before.author.avatar_url)
		await logch.send(embed=log)
		
		toeditsnipe[before.channel.id] = before.content
		toeditsnipeauthors[before.channel.id] = before.author
		timestamp2 = datetime.datetime.now()
		corfor = timestamp2.strftime("%d %b, %Y at %H:%M")
		toeditsnipetime[before.channel.id] = timestamp2


# - Afk command:
afklist = {}

@bot.command()
async def afk(ctx, *, reason: str = ""):
	#global afklist
	user = ctx.message.author
	if len(reason) == 0:
		if str(ctx.message.author.id) not in afklist.keys():
			afklist[user.id] = reason
			list = ["Fapping to pornhub.com", "Fuckin yo mom", "Doin something", "Im too lazy to type what I'm afk for", "Hi"]
			afkk = random.choice(list)
			await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, afkk))
			#return
	elif len(reason) > 0:
		if str(ctx.message.author.id) not in afklist.keys():
			afklist[user.id] = reason
			await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, reason))
			#return

# - Fun Commands:
tenorkey = "6JKJQX4V4OHD"
limit = 50
media_filter = "basic"
kiss = "animekiss"
hug = "animehug"
slap = "animeslap"
cuddle = "animecuddle"
blush = "animeblush"

kissgifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (kiss, tenorkey, limit, media_filter))
huggifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (hug, tenorkey, limit, media_filter))
slapgifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (slap, tenorkey, limit, media_filter))
cuddlegifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (cuddle, tenorkey, limit, media_filter))
blushgifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (blush, tenorkey, limit, media_filter))

kiss_gifs = json.loads(kissgifs.content)
hug_gifs = json.loads(huggifs.content)
slap_gifs = json.loads(slapgifs.content)
cuddle_gifs = json.loads(cuddlegifs.content)
blush_gifs = json.loads(blushgifs.content)
			
#print(json.dumps(kiss_gifs, sort_keys=True, indent=4))
			
@bot.command()
async def kiss(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} kisses {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(kiss_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@kiss.error
async def kiss_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll kiss you instead.", color=0x000000)
		result = random.choice(kiss_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're lonely, I'll kiss you.", color=0x000000)
		result = random.choice(kiss_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def hug(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} hugs {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(hug_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@hug.error
async def hug_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll hug you instead.", color=0x000000)
		result = random.choice(hug_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're lonely, I'll hug you.", color=0x000000)
		result = random.choice(hug_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def slap(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} slaps {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(slap_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@slap.error
async def slap_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll slap you instead.", color=0x000000)
		result = random.choice(slap_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're too weak to slap someone, so I'll slap you.", color=0x000000)
		result = random.choice(slap_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def cuddle(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} cuddles {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(cuddle_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@cuddle.error
async def cuddle_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll cuddle you instead.", color=0x000000)
		result = random.choice(cuddle_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're lonely, I'll cuddle you.", color=0x000000)
		result = random.choice(cuddle_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def blush(ctx):
	embed = discord.Embed(title="{} blushes.".format(ctx.message.author), color=0x000000)
	result = random.choice(blush_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)

conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")

	
@bot.command()
async def define(ctx, *, term: str):
	headers = {
		'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
		'x-rapidapi-key': "41e03ab49dmsh4d6a1ebe8db51dep1009b5jsnc4d2da773e2f"
	}
	conn.request("GET", f"/define?term={term}", headers=headers)
	try:
		res = conn.getresponse()
	except:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	list = res.read()
	my_json = json.loads(list)
	
	try:
		entry = my_json["list"][0]
	except IndexError:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	if len(entry["example"]) == 0:
		entry["example"] = "-"
	
	embed = discord.Embed(title=f"Definition of {entry['word']}", description=f"``Top Definition``\n{entry['definition']}\n\n ``Example``\n{entry['example']}\n\n :thumbsup: {entry['thumbs_up']} | :thumbsdown: {entry['thumbs_down']}", color=0x000000)
	embed.set_footer(text=f"Powered by UrbanDictionary")
	embed.set_thumbnail(url=ctx.message.author.avatar_url)
	
	
	await ctx.send(embed=embed)

@define.error
async def define_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Can't define nothing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def urban(ctx, *, term: str):
	headers = {
		'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
		'x-rapidapi-key': "41e03ab49dmsh4d6a1ebe8db51dep1009b5jsnc4d2da773e2f"
	}
	conn.request("GET", f"/define?term={term}", headers=headers)
	try:
		res = conn.getresponse()
	except:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	list = res.read()
	my_json = json.loads(list)
	
	try:
		entry = my_json["list"][0]
	except IndexError:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	if len(entry["example"]) == 0:
		entry["example"] = "-"
	
	embed = discord.Embed(title=f"Definition of {entry['word']}", description=f"``Top Definition``\n{entry['definition']}\n\n ``Example``\n{entry['example']}\n\n :thumbsup: {entry['thumbs_up']} | :thumbsdown: {entry['thumbs_down']}", color=0x000000)
	embed.set_footer(text=f"Powered by UrbanDictionary")
	embed.set_thumbnail(url=ctx.message.author.avatar_url)
	
	
	await ctx.send(embed=embed)

@urban.error
async def urban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Can't define nothing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def penis(ctx, *, user: discord.Member):
	sizes = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D"]
	size = random.choice(sizes)
	embed = discord.Embed(description=f"{user}'s pee pee size \n\n{size}", color=0x000000)
	embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)

@penis.error
async def penis_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        sizes = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D"]
        size = random.choice(sizes)
        embed = discord.Embed(description=f"{ctx.message.author}'s pee pee size \n\n{size}", color=0x000000)
        embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("$ dy", "Bot Coder")
async def say(ctx, chan: discord.TextChannel, *, msg: str=""):
	#channels = ctx.message.channel_mentions
	#if len(channels) > 0:
		#for channel in channels:
	await ctx.message.delete()
	try:
		await chan.send(f"{msg}")
	except discord.HTTPException as exception:
		ilove = ["Shiki", "Dy"]
		you = random.choice(ilove)
		await chan.send(f"I love {you}.")
	

@say.error
async def say_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		tosend = ctx.message.content[5:]
		await ctx.message.delete()
		await ctx.send(f"{tosend}")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		ilove = ["Shiki", "Dy"]
		you = random.choice(ilove)
		await ctx.send(f"I love {you}.")
	elif isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def thotrate(ctx, *, user: discord.Member):
    les = random.randint(0, 100)
    embed = discord.Embed(description="{} is a **{}**% thot. <:shiki_is_cool:612767957570945024>".format(user.mention, str(les)),
                          color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@thotrate.error
async def thotrate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        les = random.randint(0, 100)
        embed = discord.Embed(
            description="{} is a **{}**% thot. <:shiki_is_cool:612767957570945024>".format(ctx.message.author.mention, str(les)),
            color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def howlesbian(ctx, *, user: discord.Member):
    les = random.randint(0, 100)
    embed = discord.Embed(description="{} is **{}**% lesbian. <:lesbian22:612745721883656203>".format(user.mention, str(les)),
                          color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@howlesbian.error
async def howlesbian_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        les = random.randint(0, 100)
        embed = discord.Embed(
            description="{} is **{}**% lesbian. <:lesbian22:612745721883656203>".format(ctx.message.author.mention, str(les)),
            color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def ping(ctx):
    #print("Testing ping!")
    delta = datetime.datetime.now() - ctx.message.created_at
    delta_ping = round(delta.microseconds / 1000)
    if delta_ping < 100:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0x00ff00)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.message.channel.send(embed=embed)
        return
    elif delta_ping < 200:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0xfe9a2e)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await message.channel.send(embed=embed)
        return
    else:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0xff0000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.message.channel.send(embed=embed)
		
@bot.command(name="8ball")
async def ball(ctx, *, message: str):
	if len(message) > 0:
		responds = ["yes duh", "no wtf", "ig?", "naw", "pew pew", "ur mom a hoe", "u retarded fuck, its obv yes", "ew, no", "ur pp smol", "ye", "no u", "as i see it nigga, yes", "without a fucking doubt", "tbh most likely", "sorry to inform that its a yes", "i doubt that fr", "ofc its a fucking no", "sorry nigga, but its a no", "what the fuck"]
		choice = random.choice(responds)
		embed1 = discord.Embed(description="__8Ball__\n\n...", color=0xffffff)
		embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		msg = await ctx.send(embed=embed1)
		await asyncio.sleep(1)
		embed2 = discord.Embed(description="__8Ball__\n\n**{}**".format(choice), color=0xf252e8)
		embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await msg.edit(embed=embed2)
	else:
		embed1 = discord.Embed(description="__8Ball__\n\nI couldn't answer you because you didn't give me a question.", color=0x000000)
		embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed1)
		
@ball.error
async def ball_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="__8Ball__\n\nI couldn't answer you because you didn't give me a question.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def roast(ctx, *, user: discord.Member):
	responds = ["are you sure youre not mentally retarded?", "that's gay..", "can't roast him, he doesn't have parents", "this is why no one likes you", "just stfu retard", "they got no balls dawg", "can u speak chong bong?", "what u want pussy?", "!!", "couldn't roast"]
	choice = random.choice(responds)
	embed2 = discord.Embed(description="{}".format(choice), color=0xf252e8)
	embed2.set_author(name="{}".format(user), icon_url=user.avatar_url)
	embed2.set_footer(text="Roasted by {}".format(ctx.message.author))
	await ctx.send(embed=embed2)
		
@roast.error
async def roast_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member. No roasing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Give me a member to roast.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def ship(ctx, user: discord.Member, user2: discord.Member):
    percent = random.randint(0, 100)
    strr = " "
    if percent < 11 and percent > 0:
        strr = "horrible"
    if percent < 21 and percent > 10:
        strr = "very bad"
    if percent < 31 and percent > 20:
        strr = "bad"
    if percent < 41 and percent > 30:
        strr = "worse than avarage"
    if percent < 51 and percent > 40:
        strr = "avarage"
    if percent < 61 and percent > 50:
        strr = "better than avarage"
    if percent == 69:
        strr = ":wink:"
    if percent < 71 and percent > 69 and percent < 69 and percent > 60:
        strr = "good"
    if percent < 81 and percent > 70:
        strr = "very good"
    if percent < 91 and percent > 80:
        strr = "almost perfect"
    if percent < 101 and percent > 90:
        strr = "amazing"
    embed = discord.Embed(title=":two_hearts:  MATCHMAKING: :two_hearts: ", description="**{}** :heart: **{}**\n\n**{}%**! That's **{}**.".format(user.name, user2.name, str(percent), strr), color=0x000000)
    await ctx.send(embed=embed)

@ship.error
async def ship_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="You didn't give me 2 correct users.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You didn't give me 2 users.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def rate(ctx, who, *, user: discord.Member):
    if who == "dy":
        cool = random.randint(0,10)
        embed = discord.Embed(title="👀", description="{} is a **{}**/10.".format(user.mention, str(cool)), color=0xffffff)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    #    embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Rated by Dy")
        await ctx.send(embed=embed)
        return
    if who == "shiki":
        cool = random.randint(0,10)
        embed = discord.Embed(title="<:thonk:611367036282732574>", description="{} is a **{}**/10. <a:smileg:611367087201320991>".format(user.mention, str(cool)), color=0x4287f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    #    embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Rated by Shiki")
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(description="You didn't provide a valid argument, ``rate`` accepts only **dy** and **shiki**.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return

@rate.error
async def rate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You actually have to give me a member to rate.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def howgay(ctx, *, user: discord.Member):
    gay = random.randint(0,100)
    embed = discord.Embed(description="{} is **{}**% gay. :gay_pride_flag:".format(user.mention, str(gay)), color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@howgay.error
async def howgay_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Just give me a member and I'll tell you their gayness.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def coinflip(ctx):
    embed1 = discord.Embed(description="Flipping... \n\nResults:", color=0xffffff)
    embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed1)
    await asyncio.sleep(5)
    rn = random.randint(0,100)
    results = " "
    if rn < 51:
        results = "HEADS"
    if rn > 50:
        results = "TAILS"
    embed2 = discord.Embed(description="Flipped. \n\nResults: **{}**.".format(results), color=0xe9f542)
    embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await msg.edit(embed=embed2)

@bot.command()
async def cf(ctx):
    embed1 = discord.Embed(description="Flipping... \n\nResults:", color=0xffffff)
    embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed1)
    await asyncio.sleep(5)
    rn = random.randint(0,100)
    results = " "
    if rn < 51:
        results = "HEADS"
    if rn > 50:
        results = "TAILS"
    embed2 = discord.Embed(description="Flipped. \n\nResults: **{}**.".format(results), color=0xe9f542)
    embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await msg.edit(embed=embed2)

@bot.command()
async def snipe(ctx):
	for key in tosnipe:
		if key == ctx.message.channel.id:
			msg = tosnipe[key]
			author = tosnipeauthors[key]
			time = tosnipetime[key]
			embed = discord.Embed(description="{}".format(str(msg)), color=0x000000)
			embed.set_author(name="{}".format(author), icon_url=author.avatar_url)
			corfor = time.strftime("%d %b, %Y at %H:%M")
			embed.set_footer(text="{}".format(str(corfor)))
			await ctx.send(embed=embed)

@bot.command()
async def editsnipe(ctx):
	for key in toeditsnipe:
		if key == ctx.message.channel.id:
			msg = toeditsnipe[key]
			author = toeditsnipeauthors[key]
			time = toeditsnipetime[key]
			embed = discord.Embed(description="{}".format(str(msg)), color=0x000000)
			embed.set_author(name="{}".format(author), icon_url=author.avatar_url)
			corfor = time.strftime("%d %b, %Y at %H:%M")
			embed.set_footer(text="{}".format(str(corfor)))
			await ctx.send(embed=embed)

# - Reminder Commands:
remindersserver = []

@bot.command()
async def reminder(ctx, intime, *, remindmsg: str=""):
	if ctx.message.author.id in remindersserver:
		embed = discord.Embed(description="You already have an ongoing reminder! If you want to make a new one, you have to remove the old one using ``!remindercancel``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	if len(remindmsg) == 0:
			embed = discord.Embed(description="Fatal error. Check the ``message`` parameter and try again. Please note that __you need to give me a message to remind you with__.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		n = intime[:-1]
		type = intime[-1]

		try:
			number = int(n)
		except:
			embed = discord.Embed(description="Fatal error. Check the ``time`` parameter and try again. Please note that **this is a correct format**: 3s (3 seconds), 5m (5 minutes), 7h (7 hours), 1d (1 day). There is also a limit of 7 days.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		if type == "s":
			if number > 604800:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** second(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number))
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "m":
			if number > 10080:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** minute(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60)
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "h":
			if number > 168:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** hour(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60)
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "d":
			if number > 7:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** day(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60 * 24)
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
				
@reminder.error
async def reminder_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="Fatal error. Are you sure you're giving me a member?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You're missing required arguments. Here's an example of how to use this command: \n``!reminder 3h going to appreciate this godly command``", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def remindercancel(ctx):
	if ctx.message.author.id in remindersserver:
		embed = discord.Embed(description="Reminder successfully canceled.", color=0xffffff)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		remindersserver.remove(ctx.message.author.id)
	else:
		embed = discord.Embed(description="You don't have a reminder to cancel. Set one by using ``!reminder``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)

remindersdm = []

@bot.command()
async def reminderdm(ctx, intime, *, remindmsg: str=""):
	if ctx.message.author.id in remindersdm:
		embed = discord.Embed(description="You already have an ongoing reminder! If you want to make a new one, you have to remove the old one using ``!remindercancel``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	if len(remindmsg) == 0:
			embed = discord.Embed(description="Fatal error. Check the ``message`` parameter and try again. Please note that __you need to give me a message to remind you with__.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		n = intime[:-1]
		type = intime[-1]
		
		try:
			number = int(n)
		except:
			embed = discord.Embed(description="Fatal error. Check the ``time`` parameter and try again. Please note that **this is a correct format**: 3s (3 seconds), 5m (5 minutes), 7h (7 hours), 1d (1 day). There is also a limit of 7 days.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		if type == "s":
			if number > 604800:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** second(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number))
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "m":
			if number > 10080:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** minute(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60)
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "h":
			if number > 168:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** hour(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60)
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "d":
			if number > 7:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** day(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60 * 24)
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
				
@reminderdm.error
async def reminderdm_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="Fatal error. Are you sure you're giving me a member?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You're missing required arguments. Here's an example of how to use this command: \n``!reminder 3h going to appreciate this godly command``", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def reminderdmcancel(ctx):
	if ctx.message.author.id in remindersserver:
		embed = discord.Embed(description="DM reminder successfully canceled.", color=0xffffff)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		remindersdm.remove(ctx.message.author.id)
	else:
		embed = discord.Embed(description="You don't have a DM reminder to cancel. Set one by using ``!reminderdm``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)

# - Verify command:
@bot.command()
@commands.has_any_role("Head Admin ✧˚*:･", "Co Owner ‧₊˚ ༄", "Bot Coder", "$ dy")
async def verify(ctx, user: discord.Member, gender: str=" "):
	verm = discord.utils.get(ctx.message.author.guild.roles, name="Verified Male")
	verf = discord.utils.get(ctx.message.author.guild.roles, name="Verified Female")

	failtover = discord.Embed(description="Try verifying this member again, but specify either **f** / **female** or **m** / **male**. \nExample: ``!verify @cooluser m``", color=0xFF3639)
	failtover.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	failtover.set_footer(text="Error raised on: {}".format(ctx.message.content))
	
	alrver = discord.Embed(description="This user is already verified.", color=0xFF3639)
	alrver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	alrver.set_footer(text="Error raised on: {}".format(ctx.message.content))
	if(verm in user.roles or verf in user.roles):
		await ctx.message.delete()
		msg = await ctx.send(embed=alrver)
		await asyncio.sleep(float(10))
		await msg.delete()
		return
	if(gender == "m" or gender == "male"):
		#verr = " ".join(m)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Male** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verm)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	elif(gender == "f" or gender == "female"):
		#verr = " ".join(f)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has rece9ved the **Verified Female** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verf)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	else:
		await ctx.message.delete()
		fail = await ctx.send(embed=failtover)
		await asyncio.sleep(float(10))
		await fail.delete()
		return
	
@verify.error
async def verify_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Try again, but give me a user to verify.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg =await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
@commands.has_any_role("Head Admin ✧˚*:･", "Co Owner ‧₊˚ ༄", "Bot Coder", "$ dy")
async def v(ctx, user: discord.Member, gender: str=" "):
	verm = discord.utils.get(ctx.message.author.guild.roles, name="Verified Male")
	verf = discord.utils.get(ctx.message.author.guild.roles, name="Verified Female")
	verchan = discord.utils.get(ctx.message.author.guild.channels, name="♡│verification")

	failtover = discord.Embed(description="Try verifying this member again, but specify either **f** / **female** or **m** / **male**. \nExample: ``!verify @cooluser m``", color=0xFF3639)
	failtover.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	failtover.set_footer(text="Error raised on: {}".format(ctx.message.content))
	
	alrver = discord.Embed(description="This user is already verified.", color=0xFF3639)
	alrver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	alrver.set_footer(text="Error raised on: {}".format(ctx.message.content))
	if(verm in user.roles or verf in user.roles):
		await ctx.message.delete()
		msg = await ctx.send(embed=alrver)
		await asyncio.sleep(float(10))
		await msg.delete()
		return
	if(gender == "m" or gender == "male"):
		#verr = " ".join(m)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Male** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verm)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	elif(gender == "f" or gender == "female"):
		#verr = " ".join(f)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Female** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verf)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	else:
		await ctx.message.delete()
		fail = await ctx.send(embed=failtover)
		await asyncio.sleep(float(10))
		await fail.delete()
		return
	
@v.error
async def v_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Try again, but give me a user to verify.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg =await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Info commands:

@bot.command()
async def membercount(ctx):
	time = datetime.datetime.now()
	corfor = time.strftime("%d %b, %Y at %H:%M")
	
	online = 0
	for member in ctx.message.author.guild.members:
		if member.status != discord.Status.offline:
			online += 1
	bots = 0
	for member in ctx.message.author.guild.members:
		if member.bot == True:
			bots += 1
	humans = 0
	for member in ctx.message.author.guild.members:
		if member.bot == False:
			humans += 1
	
	embed = discord.Embed(color=0x000000)
	embed.add_field(name="Members", value="{}".format(ctx.message.author.guild.member_count), inline=True)
	embed.add_field(name="Online", value="{}".format(online), inline=True)
	embed.add_field(name="Humans", value="{}".format(humans), inline=True)
	embed.add_field(name="Bots", value="{}".format(bots), inline=True)
	embed.set_footer(text="ID: {} | {}".format(ctx.message.author.guild.id, corfor))
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)

	await ctx.send(embed=embed)


@bot.command()
async def serverinfo(ctx):
	time = ctx.message.author.guild.created_at 
	
	corfor = time.strftime("%d %b, %Y at %H:%M")
	
	channels = ctx.message.author.guild.text_channels
	voicechans = ctx.message.author.guild.voice_channels
	categories = ctx.message.author.guild.categories
	roles = ctx.message.author.guild.roles
	online = 0
	for member in ctx.message.author.guild.members:
		if member.status != discord.Status.offline:
			online += 1
	bots = 0
	for member in ctx.message.author.guild.members:
		if member.bot == True:
			bots += 1
	humans = 0
	for member in ctx.message.author.guild.members:
		if member.bot == False:
			humans += 1
	#fa = " "
	if ctx.message.author.guild.mfa_level == 0:
		fa = "No"
	if ctx.message.author.guild.mfa_level == 1:
		fa = "Yes"
	#ver = " "

	embed = discord.Embed(title="Info of {}".format(ctx.message.author.guild.name), description="Owned by {}".format(ctx.message.author.guild.owner), color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
	embed.set_footer(text="ID: {} | Created at: {}".format(ctx.message.author.guild.id, corfor))
	embed.add_field(name="Server region", value="{}".format(ctx.message.author.guild.region), inline=True)
	embed.add_field(name="Channels count", value="{}".format(len(channels)), inline=True)
	embed.add_field(name="Voice channels count", value="{}".format(len(voicechans)), inline=True)
	embed.add_field(name="Categories count", value="{}".format(len(categories)), inline=True)
	embed.add_field(name="Roles count", value="{}".format(len(roles)), inline=True)
	embed.add_field(name="Members", value="{}".format(ctx.message.author.guild.member_count), inline=True)
	embed.add_field(name="Online", value="{}".format(online), inline=True)
	embed.add_field(name="Humans", value="{}".format(humans), inline=True)
	embed.add_field(name="Bots", value="{}".format(bots), inline=True)
	#embed2 = discord.Embed(color=0x000000)
	embed.add_field(name="Requires 2FA", value="{}".format(fa), inline=True)
	embed.add_field(name="Boosters", value="{}".format(ctx.message.author.guild.premium_subscription_count), inline=True)
	embed.add_field(name="Boost level", value="{}".format(ctx.message.author.guild.premium_tier), inline=True)
	if str(ctx.message.author.guild.verification_level) == "none":
		ver = "None"
		embed.add_field(name="Verification level", value="{}".format(ver))
		#print(ver)
	elif str(ctx.message.author.guild.verification_level) == "low":
		ver = "Must have a verified email"
		embed.add_field(name="Verification level", value="{}".format(ver))
	elif str(ctx.message.author.guild.verification_level) == "medium":
		ver = "Must have a verified email and be registered for 5 mins"
		embed.add_field(name="Verification level", value="{}".format(ver))
	elif str(ctx.message.author.guild.verification_level) == "high":
		ver = "Must have a verified email, be registered for 5 minutes and be a member for 10 mins"
		embed.add_field(name="Verification level", value="{}".format(ver))
	elif str(ctx.message.author.guild.verification_level) == "extreme":
		ver = "Must have a verified phone number"
		embed.add_field(name="Verification level", value="{}".format(ver))
	
	await ctx.send(embed=embed)
	#await ctx.send(embed=embed2)

@bot.command()
async def bots(ctx):
	if ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089:
		bots = []
		for member in ctx.message.author.guild.members:
			if member.bot:
				bots.append(member.mention)
		embed = discord.Embed(title="All bots in this server:", description="\n".join(bots), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=bot.user.avatar_url)
		try:
			await ctx.send(embed=embed)
		except discord.HTTPException as exception:
			embed = discord.Embed(description="Too many bots, can't send the message.", color=FF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		
@bot.command()
@commands.has_any_role("Admin ˚｡☆")
async def members(ctx, *, rolee: str):
	role = await parse_roles(ctx, rolee)
	members = []
	for member in ctx.message.author.guild.members:
		if role in member.roles:
			members.append(member.mention)
	embed = discord.Embed(title="All members that have the {} role:".format(str(role)), description="\n".join(members), color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url=bot.user.avatar_url)
	try:
		await ctx.send(embed=embed)
	except discord.HTTPException as exception:
		embed = discord.Embed(description="Too many members, can't send the message.", color=-xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		
@members.error
async def members_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this role.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    # await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You didn't give me a role to get the members of.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    # await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Fun commands:
@bot.command()
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="Member not found, ping a user to get their avatar.", color=0xFF3639)
		#embed.set_image(url=bot.user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Avatar of {}".format(ctx.message.author), color=0x000000)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def av(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@av.error
async def av_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="Member not found, ping a user to get their avatar.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Avatar of {}".format(ctx.message.author), color=0x000000)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def avatarid(ctx, id: int):
	try:
		user = await bot.fetch_user(id)
	except discord.HTTPException:
		embed = discord.Embed(description="I dunno man, it doesn't look like there's a member like this.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
		
@avatarid.error    
async def avatarid_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't get the avatar of.. no one? Try giving me an ID so I can get an avatar..", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def avid(ctx, id: int):
	try:
		user = await bot.fetch_user(id)
	except discord.HTTPException:
		embed = discord.Embed(description="I dunno man, it doesn't look like there's a member like this.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
		
@avid.error    
async def avid_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't get the avatar of.. no one? Try giving me an ID so I can get an avatar..", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Admin commands: 

@bot.command()
@commands.has_any_role("Co Owner ‧₊˚ ༄", "$ dy", "scopes", "Bot Coder")
async def lockdown(ctx):
	enightclubrole = discord.utils.get(ctx.message.guild.roles, name="@everyone")
	check = ctx.message.channel.overwrites_for(enightclubrole)
	if check.send_messages == False:
		await ctx.send(":warning: **e - nightclub** | **Lockdown** mode turned __off__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=True)
	elif check.send_messages == True:
		await ctx.send(":warning: **e - nightclub** | **Lockdown** mode turned __on__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=False)
	else:
		await ctx.send(":warning: **e - nightclub** | **Lockdown** mode turned __on__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=False)

@lockdown.error
async def lockdown_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send("{} sorry but this command is for owners, co-owners, and the developer only.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Head Admin ✧˚*:･")
async def ban(ctx, user: discord.Member, *, reason: str = ""):
	if len(reason) == 0:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**. \nThe reason of their ban is **none, not provided**. \n Banned for permanent.".format(user.mention), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
		try:
			embed = discord.Embed(title="You were banned from e - nightclub.", description="You were banned by **{}**. \nThe reason for your ban is **none, not provided**. \nThis ban is permanent. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)	
	else:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**. \nThe reason of their ban is **{}**. \n Banned for permanent.".format(user.mention, reason), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		try:
			embed = discord.Embed(title="You were banned from e - nightclub.", description="You were banned by **{}**. \nThe reason for your ban is **{}**. \nThis ban is permanent. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author, reason), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	await user.ban()

@ban.error    
async def ban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. \nTIP: If you want to ban a user that's not in the server, try using !banid.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Give me a user to ban. \n``TIP:`` If you want to ban a user that's not in the server, try using !banid.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Head Admin ✧˚*:･")
async def banid(ctx, id: int, *, reason: str = " "):
	user = await bot.fetch_user(id)
	if user is None:
		embed = discord.Embed(description="User doesn't exist.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		#await ctx.send(f"{ctx.message.author.mention}, this user doesn't exist.")
		return
	#banEntry = await ctx.message.guild.fetch_ban(user)
	#if BanEntry is None:
	#if reason is None:
	#	await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
	##	try:
	#		await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
	#	except:
	#		await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: his command bans people that are not in the server, it would make sense to not have the perms to DM them.".format(user.mention))
	#else:
	#	await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
	#	try:
	##		await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
	#	except:
	#		await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: this command bans people that are not in the server, it would make sense to not have the perms to DM them..".format(user.mention))
	if len(reason) == 0:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**. \nThe reason of their ban is **none, not provided**. \n Banned for permanent.".format(user.mention), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
		try:
			embed = discord.Embed(title="You were banned from e - nightclub.", description="You were banned by **{}**. \nThe reason for your ban is **none, not provided**. \nThis ban is permanent. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=ebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	else:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**. \nThe reason of their ban is **{}**. \n Banned for permanent.".format(user.mention, reason), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		try:
			embed = discord.Embed(title="You were banned from e - nightclub.", description="You were banned by **{}**. \nThe reason for your ban is **{}**. \nThis ban is permanent. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author, reason), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)

	await ctx.message.guild.ban(discord.Object(id=id))
	#else:
		#ctx.send(f"{ctx.message.author.mention}, seems like this user is already banned.")

@banid.error    
async def banid_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Is the ID correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Give me ID of an user to ban.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("$ dy", "Bot Coder")
async def massban(ctx, *, users: str):
	desc = "Mass ban started. May take a while. \n\n" 
	embed = discord.Embed(description=desc, color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	msg = await ctx.send(embed=embed)
	mentions = ctx.message.mentions
	for user in mentions:
		#desc = desc + "\n{}".format(user)
		try:
			await user.ban()
		except:
			#desc = desc + "\n :x: | {}".format(user)
			await ctx.send(f"Couldn't ban {user.mention} because of missing permissions.")
		#await msg.edit(embed=embed)
		
@massban.error
async def massban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Head Admin ✧˚*:･")
async def unban(ctx, id: int, *, reason: str = ""):
	#print("I got the user!")
	#print("ID: " + id)
	user = await bot.fetch_user(id)
	if user is None:
		embed = discord.Embed(description="User doesn't exist.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		#await ctx.send(f"{ctx.message.author.mention}, this user doesn't exist.")
		return
	#print("I fetched this user!")
	banEntry = await ctx.message.guild.fetch_ban(user)
	if banEntry is None:
		#print("This user is not banned!")
		#await ctx.send(f"{ctx.message.author.mention}, are you sure this user is banned?")
		embed = discord.Embed(description="This user is not banned.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	else:
		if banEntry.reason is None:
			#print("Going without a reason!")
			#await ctx.send("**{}** was __unbanned__. \n"
			#				">> Unbanned by: **{}**\n"
			#				">> Reason: **who even puts reasons on unban lol**"
			#				.format(banEntry.user, ctx.message.author.mention))
			embed = discord.Embed(title="Successfully unbanned {}".format(user), description="**{}** was unbanned from [**e - nightclub**](https://discordapp.com/invite/4UkN2Jg). \nThe reason of the unban is **reasons on unban? seems gay to me**".format(banEntry.user, ctx.message.author.mention), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		else:
			#print("Going with a reason!")
			#await ctx.send("**{}** was __unbanned__. \n"
			#				">> Unbanned by: **{}**\n"
			#				">> Reason: **{}**"
			#				.format(banEntry.user, ctx.message.author.mention, reason))
			embed = discord.Embed(title="Successfully unbanned {}".format(user), description="**{}** was unbanned from [**e - nightclub**](https://discordapp.com/invite/4UkN2Jg). \nThe reason of the unban is **{}**".format(banEntry.user, ctx.message.author.mention, reason), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		#print("I unbanned the user!")
		await ctx.message.guild.unban(banEntry.user, reason="Ban reason goes here")
		
@unban.error    
async def unban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Is the ID correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
        	#await ctx.send("{} look now, do i look like a magician? just give me the id of an user and i'll unban them \n example: ``!unban id how did this happen to begin with``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't  unban.. no one? Try giving me the ID of an user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
        	#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to unban? \n example: ``!unban id how did this happen to begin with``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Mod ˚｡⋆", "Head Admin ✧˚*:･")
async def kick(ctx, user: discord.Member, *, reason: str = ""):
	if len(reason) == 0:
		embed = discord.Embed(title="Successfully kicked {}.".format(user), description="**{}** was __kicked__ from **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**. \nThe reason of their kick is **none, not provided**.".format(user.mention), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __kicked__ from **e - nightclub**.\n>> Kicked by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got slapped justcuz**".format(user.mention, ctx.message.author.mention))
		try:
			embed = discord.Embed(title="You were kicked from [**e - nightclub**](https://discordapp.com/invite/4UkN2Jg).", description="You were kicked by **{}**. \nThe reason for your kick is **none, not provided**. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been kicked from **e - nightclub**. You were kicked by **{}**, and you were kicked for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their kick. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	else:
		embed = discord.Embed(title="Successfully kicked {}.".format(user), description="**{}** was __kicked__ from **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**. \nThe reason of their kick is **{}**.".format(user.mention, reason), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __kicked__ from **e - nightclub**.\n>> Kicked by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		try:
			embed = discord.Embed(title="You were kicked from [**e - nightclub**](https://discordapp.com/invite/4UkN2Jg).", description="You were kicked by **{}**. \nThe reason for your kick is **none, not provided**. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been kicked from **e - nightclub**. You were kicked by **{}**, and you were kicked for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their kick. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	await user.kick()
 
@kick.error    
async def kick_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll kick them \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't kick.. no one? Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to kick? \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Mod ˚｡⋆", "Chat Moderator", "Head Admin ✧˚*:･")
async def mute(ctx, user: discord.Member, *, reason: str = ""):
	mutedrole = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
	if mutedrole in user.roles:
		embed = discord.Embed(description="This user is already muted.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	else:
		if len(reason) == 0:
			embed = discord.Embed(title="Successfully muted {}.".format(user), description="**{}** was __muted__. \nThe reason of their mute is **none, not provided**.".format(user.mention), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("**{}** was __muted__.\n>> Muted by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got slapped justcuz** \n**This mute won't be removed automatically. Someone has to manually remove it.**".format(user.mention, ctx.message.author.mention))
			try:
				embed = discord.Embed(title="You were muted in [**e - nightclub**](https://discordapp.com/invite/4UkN2Jg).", description="You were muted by **{}**. \nThe reason for your mute is **none, not provided**. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author), color=0x000000)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await user.send(embed=embed)
				#await user.send("You've been muted in **e - nightclub**. You were muted by **{}**, and you were muted for **none (no reason was found)**.\n**This mute won't be removed automatically. Someone has to manually remove it.**\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
			except:
				embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				await ctx.send(embed=embed)
				#await ctx.send("I failed to DM {}, so I didn't inform them for their mute. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		else:
			embed = discord.Embed(title="Successfully muted {}.".format(user), description="**{}** was __muted__. \nThe reason of their mute is **{}**.".format(user.mention, reason), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("**{}** was __muted__.\n>> Muted by: **{}**\n>> Reason: **{}**\n**This mute won't be removed automatically. Someone has to manually remove it.**".format(user.mention, ctx.message.author.mention, reason))
			try:
				embed = discord.Embed(title="You were muted in [**e - nightclub**](https://discordapp.com/invite/4UkN2Jg).", description="You were muted by **{}**. \nThe reason for your mute is **{}**. \n\n [ - The e - nightclub staff team.](https://discordapp.com/invite/4UkN2Jg)".format(ctx.message.author, reason), color=0x000000)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await user.send(embed=embed)
				#await user.send("You've been muted in **e - nightclub**. You were muted by **{}**, and you were muted for **{}**. \n**This mute won't be removed automatically. Someone has to manually remove it.**\n If you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author, reason))
			except:
				embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				await ctx.send(embed=embed)
				#await ctx.send("I failed to DM {}, so I didn't inform them for their mute. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		await user.add_roles(mutedrole)
 
@mute.error    
async def mute_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll kick them \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't mute.. no one? Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to kick? \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Mod ˚｡⋆", "Chat Moderator", "Head Admin ✧˚*:･")
async def unmute(ctx, user: discord.Member, *, reason: str = ""):
	mutedrole = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
	if mutedrole in user.roles:
		if len(reason) == 0:
			embed = discord.Embed(title="Successfully unmuted {}.".format(user), description="**{}** was __unmuted__. \nThe reason of their unmute is **none, not provided**.".format(user.mention), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		#await ctx.send("**{}** was __unmuted__. \n>> Unmuted by: **{}**\n>> Reason: **who even puts reasons on unmute lol**".format(user.mention, ctx.message.author.mention))
		else:
			embed = discord.Embed(title="Successfully unmuted {}.".format(user), description="**{}** was __unmuted__. \nThe reason of their unmute is **{}**.".format(user.mention, reason), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		#await ctx.send("**{}** was __unmuted__. \n>> Unmuted by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		await user.remove_roles(mutedrole)
	else:
		embed = discord.Embed(description="This user is not muted.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return

@unmute.error    
async def unmute_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
 		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll unmute them \n example: ``!unmute @dy lol begged for unmute``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't unmute.. no one? Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to unmute? \n example: ``!unmute @dy lol begged for unmute``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Userinfo Command:
def sort_by_joined_at(member:discord.Member):
	return member.joined_at
	
@bot.command()
async def userinfo(ctx, user: discord.Member):
	time = user.joined_at
	
	corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
	time2 = user.created_at
	
	corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
	memberslist = ctx.guild.members
	memberslist.sort(key=sort_by_joined_at)
	joinpos = memberslist.index(user)
	
	boosting = " "
	if user.premium_since == None:
		boosting = "Nope"
	else:
		time3 = user.premium_since
		corfor3 = time3.strftime("%d %b, %Y at %H:%M")
		boosting = "Yes"
		
	fro = " "
	if user.is_on_mobile():
		fro = "Mobile"
	else:
		fro = "PC"
	
	embed = discord.Embed(description="Nickname: {}".format(user.nick), color=0x000000)
	embed.set_author(name="Info of {}".format(user), icon_url=user.avatar_url)
	embed.set_footer(text="Requested by {}".format(ctx.message.author))
	embed.add_field(name="Joined on", value="{}".format(corfor1))
	embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
	embed.add_field(name="Registered on", value="{}".format(corfor2))
	embed.add_field(name="Boosting this guild", value="{}".format(boosting))
	embed.add_field(name="Current status", value="{}".format(str(user.status)))
	embed.add_field(name="Mobile or PC", value="{}".format(fro))
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@userinfo.error    
async def userinfo_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="Member not found, check the member you gave me and try again.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		time = ctx.message.author.joined_at
	
		corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
		time2 = ctx.message.author.created_at
	
		corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
		memberslist = ctx.guild.members
		memberslist.sort(key=sort_by_joined_at)
		joinpos = memberslist.index(ctx.message.author)
	
		boosting = " "
		if ctx.message.author.premium_since == None:
			boosting = "Nope"
		else:
			time3 = ctx.message.author.premium_since
			corfor3 = time3.strftime("%d %b, %Y at %H:%M")
			boosting = "Yes"
		
		fro = " "
		if ctx.message.author.is_on_mobile():
			fro = "Mobile"
		else:
			fro = "PC"
	
		embed = discord.Embed(description="Nickname: {}".format(ctx.message.author.nick), color=0x000000)
		embed.set_author(name="Info of {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author))
		embed.add_field(name="Joined on", value="{}".format(corfor1))
		embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
		embed.add_field(name="Registered on", value="{}".format(corfor2))
		embed.add_field(name="Boosting this guild", value="{}".format(boosting))
		embed.add_field(name="Current status", value="{}".format(str(ctx.message.author.status)))
		embed.add_field(name="Mobile or PC", value="{}".format(fro))
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def uf(ctx, user: discord.Member):
	time = user.joined_at
	
	corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
	time2 = user.created_at
	
	corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
	memberslist = ctx.guild.members
	memberslist.sort(key=sort_by_joined_at)
	joinpos = memberslist.index(user)
	
	boosting = " "
	if user.premium_since == None:
		boosting = "Nope"
	else:
		time3 = user.premium_since
		corfor3 = time3.strftime("%d %b, %Y at %H:%M")
		boosting = "Yes"
		
	fro = " "
	if user.is_on_mobile():
		fro = "Mobile"
	else:
		fro = "PC"
	
	embed = discord.Embed(description="Nickname: {}".format(user.nick), color=0x000000)
	embed.set_author(name="Info of {}".format(user), icon_url=user.avatar_url)
	embed.set_footer(text="Requested by {}".format(ctx.message.author))
	embed.add_field(name="Joined on", value="{}".format(corfor1))
	embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
	embed.add_field(name="Registered on", value="{}".format(corfor2))
	embed.add_field(name="Boosting this guild", value="{}".format(boosting))
	embed.add_field(name="Current status", value="{}".format(str(user.status)))
	embed.add_field(name="Mobile or PC", value="{}".format(fro))
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@uf.error
async def uf_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="Member not found, check the member you gave me and try again.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		time = ctx.message.author.joined_at
	
		corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
		time2 = ctx.message.author.created_at
	
		corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
		memberslist = ctx.guild.members
		memberslist.sort(key=sort_by_joined_at)
		joinpos = memberslist.index(ctx.message.author)
	
		boosting = " "
		if ctx.message.author.premium_since == None:
			boosting = "Nope"
		else:
			time3 = ctx.message.author.premium_since
			corfor3 = time3.strftime("%d %b, %Y at %H:%M")
			boosting = "Yes"
		
		fro = " "
		if ctx.message.author.is_on_mobile():
			fro = "Mobile"
		else:
			fro = "PC"
	
		embed = discord.Embed(description="Nickname: {}".format(ctx.message.author.nick), color=0x000000)
		embed.set_author(name="Info of {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author))
		embed.add_field(name="Joined on", value="{}".format(corfor1))
		embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
		embed.add_field(name="Registered on", value="{}".format(corfor2))
		embed.add_field(name="Boosting this guild", value="{}".format(boosting))
		embed.add_field(name="Current status", value="{}".format(str(ctx.message.author.status)))
		embed.add_field(name="Mobile or PC", value="{}".format(fro))
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def whois(ctx, user: discord.Member):
	time = user.joined_at
	
	corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
	time2 = user.created_at
	
	corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
	memberslist = ctx.guild.members
	memberslist.sort(key=sort_by_joined_at)
	joinpos = memberslist.index(user)
	
	boosting = " "
	if user.premium_since == None:
		boosting = "Nope"
	else:
		time3 = user.premium_since
		corfor3 = time3.strftime("%d %b, %Y at %H:%M")
		boosting = "Yes"
		
	fro = " "
	if user.is_on_mobile():
		fro = "Mobile"
	else:
		fro = "PC"
	
	embed = discord.Embed(description="Nickname: {}".format(user.nick), color=0x000000)
	embed.set_author(name="Info of {}".format(user), icon_url=user.avatar_url)
	embed.set_footer(text="Requested by {}".format(ctx.message.author))
	embed.add_field(name="Joined on", value="{}".format(corfor1))
	embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
	embed.add_field(name="Registered on", value="{}".format(corfor2))
	embed.add_field(name="Boosting this guild", value="{}".format(boosting))
	embed.add_field(name="Current status", value="{}".format(str(user.status)))
	embed.add_field(name="Mobile or PC", value="{}".format(fro))
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@whois.error
async def whois_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="Member not found, check the member you gave me and try again.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		time = ctx.message.author.joined_at
	
		corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
		time2 = ctx.message.author.created_at
	
		corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
		memberslist = ctx.guild.members
		memberslist.sort(key=sort_by_joined_at)
		joinpos = memberslist.index(ctx.message.author)
	
		boosting = " "
		if ctx.message.author.premium_since == None:
			boosting = "Nope"
		else:
			time3 = ctx.message.author.premium_since
			corfor3 = time3.strftime("%d %b, %Y at %H:%M")
			boosting = "Yes"
		
		fro = " "
		if ctx.message.author.is_on_mobile():
			fro = "Mobile"
		else:
			fro = "PC"
	
		embed = discord.Embed(description="Nickname: {}".format(ctx.message.author.nick), color=0x000000)
		embed.set_author(name="Info of {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author))
		embed.add_field(name="Joined on", value="{}".format(corfor1))
		embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
		embed.add_field(name="Registered on", value="{}".format(corfor2))
		embed.add_field(name="Boosting this guild", value="{}".format(boosting))
		embed.add_field(name="Current status", value="{}".format(str(ctx.message.author.status)))
		embed.add_field(name="Mobile or PC", value="{}".format(fro))
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def status(ctx, a, b, *, status: str=" "):
	if(ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089):
		if len(a) != 0:
			#embed = discord.Embed(description="Status changed. \n".format(status), color=0x000000)
			if ((a == "o" or a =="online") and (b == "p" or b == "playing")):
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
			elif ((a == "o" or a == "online") and (b == "w" or b == "watching")):
				embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.watching))
			elif ((a == "o" or a =="online") and (b == "l" or b == "listening")):
				embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.listening))
			elif ((a == "i" or a =="idle") and (b == "p" or b == "playing")):
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
			elif ((a == "i" or a == "idle") and (b == "w" or b == "watching")):
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Watching {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.watching))
			elif ((a == "i" or a =="idle") and (b == "l" or b == "listening")):
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Listening to {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.listening))
			elif ((a == "d" or a =="dnd") and (b == "p" or b == "playing")):
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
			elif ((a == "d" or a == "dnd") and (b == "w" or b == "watching")):
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Watching {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.watching))
			elif ((a == "d" or a =="dnd") and (b == "l" or b == "listening")):
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Listening to {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.listening))
			elif (a == "o" or a =="online"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 6:
					statuss = ctx.message.content[14:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "i" or a == "idle"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 4:
					statuss = ctx.message.content[12:]
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "d" or a =="dnd"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 3:
					statuss = ctx.message.content[11:]
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "playing" or a == "p"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 7:
					statuss = ctx.message.content[15:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_ttpe**, I chose the default one: **Online**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "w" or a == "watching"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 8:
					statuss = ctx.message.content[16:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.watching))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "l" or a == "listening"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 9:
					statuss = ctx.message.content[17:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.listening))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			else:
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type** and/or **status_msg** combination, I chose the default ones: **Online** and **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))

			
			
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await ctx.send(embed=embed)
			#await bot.change_presence(activity=discord.Game(name='{}'.format(status)))
		else:
			embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
			embed.set_image(url=ctx.message.author.guild.icon_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
@status.error
async def status_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		if(ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089):
			if len(ctx.message.content) > 8:
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
				status = ctx.message.content[7:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
		else:
			embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	if isinstance(error, commands.MissingRequiredArgument):
		#embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		#embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		#embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		#await ctx.send(embed=embed)
		if(ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089):
			if len(ctx.message.content) > 8:
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
				status = ctx.message.content[7:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
		else:
			embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Role Command:

async def parse_roles(ctx, role:str):
	try:
		id: int = int(role)
		role = ctx.guild.get_role(id)
		if role is not None:
			return role
	except ValueError:
		pass
	for guild_role in ctx.guild.roles:
		if role.lower() == guild_role.name.lower():
			return guild_role
	for guild_role in ctx.guild.roles:
		if role.lower() in guild_role.name.lower():
			return guild_role
	return None

@bot.command()
@commands.has_any_role("Role Perms")
async def role(ctx, user: discord.Member, *, rolee: str):
    role = await parse_roles(ctx, rolee)
    if role is None:
        embed = discord.Embed(description="You didn't give me a correct role.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    if role in user.roles:
        embed = discord.Embed(
            description="Successfully removed the **{}** role from **{}**.".format(str(role), user.mention),
            color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
        await user.remove_roles(role)
        logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
        timestamp = datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(description="Used command ``!role`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
    else:
        embed = discord.Embed(
            description="Successfully added the **{}** role to **{}**.".format(str(role), user.mention),
            color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
        await user.add_roles(role)
        logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
        timestamp = datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(description="Used command ``!role`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
	
@role.error    
async def role_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="You didn't give me a correct user and/or a role.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="You didn't give me a user and/or a role.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	elif isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Purge Command:
@bot.command()
@commands.has_any_role("Chat Moderator", "Mod ˚｡⋆", "Admin ˚｡☆", "Head Admin ✧˚*:･")
async def clean(ctx):
	def check(m):
		return m.author.bot
	#rr = todeln + 1
	deleted = await ctx.message.channel.purge(limit=100, check=check)
	embed = discord.Embed(description="Cleaned bot's messages.", color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	await ctx.send(embed=embed)
	
@clean.error
async def clean_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Chat Moderator", "Mod ˚｡⋆", "Admin ˚｡☆", "Head Admin ✧˚*:･")
async def purge(ctx, amount, *, user: discord.Member):
	try:
		todeln = int(amount)
	except:
		embed = discord.Embed(description="You didn't enter a number between 2 and 200.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	if(todeln < 200 and todeln > 0):
		def check(m):
			return m.author == user
		#rr = todeln + 1
		deleted = await ctx.message.channel.purge(limit=todeln, check=check)
		embed = discord.Embed(description="Successfully purged **{}** messages by **{}**.".format(todeln, user.mention), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=user.avatar_url)
		await ctx.send(embed=embed)
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!purge`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
		
@purge.error
async def purge_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		todeln = int(ctx.message.content[7:])
		if(todeln < 200 and todeln > 2):
			deleted = await ctx.message.channel.purge(limit=(todeln + 1))
			embed = discord.Embed(description="Successfully purged **{}** messages.".format(todeln), color=0x000000)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!purge`` in {}:\n{}\n\nMod ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			#log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
			return
		else:
			embed = discord.Embed(description="There's a limit of 200 messages per purge. You entered a higher number than that.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - BOT LOGIN


bot.run("TOKEN")
