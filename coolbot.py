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

    await bot.change_presence(activity=discord.Game(name='with dy & shiki >_<'))
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
        embed3 = discord.Embed(title="Reminder:", description="If you want to apply for **Partnership Mananger** or **Server Helper**, type **!apply** in {}.".format(apply), color=0xffffff)
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
        channel = discord.utils.get(member.guild.channels, name="☆│lounge")
        channel2 = discord.utils.get(member.guild.channels, name="✵│welcome-rules")
        channel3 = discord.utils.get(member.guild.channels, name="∞│roles-menu")
        channel4 = discord.utils.get(member.guild.channels, name="✵│faq")
        embed = discord.Embed(description="Welcome to **[e - nightclub](https://discordapp.com/invite/4UkN2Jg)**! You're the **{}th** member. \n\n Make sure to read: {}  \n\nRoles: {}  \n\nFor help:  {}.".format(member.guild.member_count, channel2.mention, channel3.mention, channel4.mention), color=0x000000)
        embed.set_author(name="{}".format(member), icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.guild.icon_url)
        await channel.send(embed=embed)
        #await channel.send("Welcome {} to **e nightclub!** You’re the **{}** member. \n\n Make sure to read: {}  |  Roles: {}  |  For help:  {}.".format(member.mention, member.guild.member_count, channel2.mention, channel3.mention, channel4.mention))

# leave message

@bot.event
async def on_member_remove(member):
    if(member.guild.id == 448571905524498432):
        channel = discord.utils.get(member.guild.channels, name="✵│left")
        await channel.send("**{}** has left the server. We now have **{}** members.".format(member.mention, member.guild.member_count))

# EMBED MESSAGES

@bot.event
async def on_message(message: Message):
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
    elif shiki in message.mentions:
        await message.author.send(f"Hey there, {message.author.mention}! \nPlease don't abusively mention the Devs without a reason. If you want to just talk to them, it's okay, but don't don it oftenly without a real reason. But while you're here... \n\n Are you looking for **cheap** and sometimes **free** __bot developing and hosting__? Our **custom bot**, <@593090256560193549> was made by the user you just pinged, {shiki.mention}. \n\n If you're interesting in having a custom bot like this one, **DM {shiki.mention}** and we'll talk about it there. \n\n > This automatic action was fired because you pinged either the Bot Coder role or {shiki.mention}.")
    elif message.content == "dy":
        await message.channel.send("dy >_<")
    elif message.content == "lumen":
        await message.channel.send("LUMEN XD")
    elif message.content == "shiki":
        await message.channel.send(">.<")
    elif message.content == "no u" and message.author.id != 593090256560193549:
        await message.channel.send("no u")

    await bot.process_commands(message)

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
		log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		embed = discord.Embed(description="I couldn't ban.. no one? Try giving me an user to ban. \nTIP: If you want to ban a user that's not in the server, try using !banid.", color=0xFF3639)
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
		log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		embed = discord.Embed(description="I couldn't ban.. no one? Try giving me the ID of an user.", color=0xFF3639)
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
			log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
			log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
			log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
			log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
			log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
			log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
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
		embed = discord.Embed(title="Member not found, check the member you gave me and try again. \nIf you want to get the info of a user that's not in the server, try ?userinfoid.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Try giving me a member to get the info of. \nIf you want to get the info of a user that's not in the server, try ?userinfoid.".format(ctx.message.author), color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
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
		embed = discord.Embed(title="Member not found, check the member you gave me and try again. \nIf you want to get the info of a user that's not in the server, try ?userinfoid.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Try giving me a member to get the info of. \nIf you want to get the info of a user that's not in the server, try ?userinfoid.".format(ctx.message.author), color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
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
		embed = discord.Embed(title="Member not found, check the member you gave me and try again. \nIf you want to get the info of a user that's not in the server, try ?userinfoid.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Try giving me a member to get the info of. \nIf you want to get the info of a user that's not in the server, try ?userinfoid.".format(ctx.message.author), color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
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


# - BOT LOGIN


bot.run(os.environ.get("token"))
