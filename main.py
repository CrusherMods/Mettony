import disnake 
from disnake.ext import commands
import os
import json
import random
import time
import urllib
import asyncio
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageOps
from easy_pil import Editor, Canvas, Font, font
from keep_alive import keep_alive

clientprefixes = 'mettony ', 'm!', 'susbot '
client = commands.Bot(command_prefix=clientprefixes)
client.remove_command("help")
client.sniped_messages = {}

owner = YOUR_ID_HERE #cool gang 😎😎
hafimie = FRIEND_ID_HERE #hafimie helped me LIKE A LOT so

async def setactivity():
    await client.change_presence(status=disnake.Status.idle,
                                 activity=disnake.Activity(
                                     type=disnake.ActivityType.watching,
                                     name=f"Amogus on Netflix"))
    await asyncio.sleep(4)
    await client.change_presence(status=disnake.Status.do_not_disturb,
                                 activity=disnake.Activity(
                                     type=disnake.ActivityType.playing,
                                     name=f"your dad"))
    await asyncio.sleep(4)
    await client.change_presence(status=disnake.Status.idle,
                                 activity=disnake.Activity(
                                     type=disnake.ActivityType.playing,
                                     name=f"amogus fidget toy"))
    await asyncio.sleep(4)
    await client.change_presence(status=disnake.Status.idle,
                                 activity=disnake.Activity(
                                     type=disnake.ActivityType.listening,
                                     name=f"1 hour amogus drip"))
    await asyncio.sleep(4)
    await setactivity()


@client.event
async def on_ready():
    await setactivity()
    print(f"Logged in as {client.user}!")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        cooldowntext = "Try again in {:.2f}s/m/h".format(error.retry_after)

        embed = disnake.Embed(
            title=f"Command Cooldown",
            description=f"Spamming isn't cool, {cooldowntext}.",
            color=disnake.Color.blue())
        await ctx.send(embed=embed)


@client.event
async def on_message_delete(message):
    if message.author.id == owner:
        print(
            f"======================================\nAuthor message's are deleted!\nMessage: {message.content}\nChannel: #{message.channel.name}\nTime: {message.created_at}\n======================================"
        )
        client.sniped_messages[message.guild.id] = (message.content,
                                                    message.author,
                                                    message.channel.name,
                                                    message.created_at)
    else:
        print(
            f"======================================\n{message.author} message's are deleted!\nMessage: {message.content}\nChannel: #{message.channel.name}\nTime: {message.created_at}\n======================================"
        )
        client.sniped_messages[message.guild.id] = (message.content,
                                                    message.author,
                                                    message.channel.name,
                                                    message.created_at)


@client.command(aliases=['s', 'deletedmessage', 'delm'])
async def snipe(ctx):
    contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
    embed = disnake.Embed(description=contents,
                          color=disnake.Color.blue(),
                          timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}",
                     icon_url=author.display_avatar.url)
    embed.set_footer(text=f"Deleted in: #{channel_name}")
    await ctx.channel.send(embed=embed)


@client.command()
async def say(ctx, *, say=None):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{say}")


@client.command()
async def coolm(ctx, *, user=None):
    if user is None:
        embed = disnake.Embed(
            title=f"Cool Meter 😎",
            description=f"You are {random.randrange(100)}% cool.",
            color=disnake.Colour.blue())
        await ctx.send(embed=embed)
    else:
        embed = disnake.Embed(
            title=f"Cool Meter 😎",
            description=f"{user} is {random.randrange(100)}% cool.",
            color=disnake.Colour.blue())
        await ctx.send(embed=embed)


dumbpass = 'imcool', 'hacker8281', 'someonesus13', 'notsus82828', 'haxor111111', 'sus69420', 'imgayandhomophobic111'
cmonword = 'im cool', 'lmao', 'i love my mom', 'i peed on my bed sometimes', 'cum', 'Its long'
emailsus = 'IsDumbass', 'IsIdiot', 'HasFriends', 'Piss', 'IsCool'


@client.command()
async def hack(ctx, member: disnake.Member = None):
    #  if member.id == owner or hafimie:
    #    await ctx.send("No")
    #  else:
    test = await ctx.send(f"Hacking {member.name} now...")
    await asyncio.sleep(5)
    await test.edit(content=f"Finding {member.name}'s discord login...")
    await asyncio.sleep(5)
    await test.edit(
        content=
        f"Found {member.name}'s login!\nEmail: `{member.name}{random.choice(emailsus)}`\nPassword: `{random.choice(dumbpass)}`"
    )
    await asyncio.sleep(5)
    await test.edit(content=f"Finding {member.name}'s common word...")
    await asyncio.sleep(5)
    await test.edit(
        content=
        f"{member.name}'s most common word is: `{random.choice(cmonword)}`")
    await asyncio.sleep(5)
    await test.edit(
        content="The _totally really really_ dangerous hack is completed.")


@client.command()
async def slap(ctx, member: disnake.Member = None):
    pig = Image.open('assets/slapsshit.jpg')

    asset = member.display_avatar.with_size(128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    asset2 = ctx.author.display_avatar.with_size(128)
    data2 = BytesIO(await asset2.read())
    pfp2 = Image.open(data2)

    pfp2 = pfp2.resize((197, 213))
    pfp = pfp.resize((221, 223))

    pig.paste(pfp, (213, 194))
    pig.paste(pfp2, (535, 56))

    pig.save('assets/slapping.jpg')

    await ctx.send(file=disnake.File('assets/slapping.jpg'))

    os.remove("assets/slapping.jpg")


@client.command()
async def help(ctx):
    embed = disnake.Embed(
        title=f"Help Command",
        description=
        f"**Information:**\n \nm!credits - Shows the Credits of Mettony\n\n**Utilitys:**\n\nm!snipe - Shows the Latest Deleted Message\n\n**Fun:**\n\nm!hack @Username",
        color=disnake.Colour.blue())
    embed.set_footer(
        text="Prefixes are: m!, mettony & susbot but we use m! for an example")
    await ctx.send(embed=embed)


@client.command()
async def credits(ctx):
    embed = disnake.Embed(
        title=f"Credits",
        description=
        "Owner: CrusherNotDrip#0001\nCo-Owner: Hafimie#8182\n\nNames for Beg Command: NeonFurious + anshh",
        color=disnake.Colour.blue())
    await ctx.send(embed=embed)


#IM FINALLY WATCHING TUTORIALS NOW WOHOOOOOOOO


@client.command(aliases=(['bal']))
async def balance(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    embed = disnake.Embed(
        title=f"{ctx.author.name}'s balance",
        description=f"Wallet Balance: {wallet_amt} MetoCoins \n Bank Balance: {bank_amt} MetoCoins",
        color=disnake.Colour.blue())
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def beg(ctx):

    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    dummynames = 'Crusher', 'Meeny', 'NeonFurious', 'Roboscrew', 'Candice', 'Rubma', 'The Rock', 'Mike Hawk', 'Tom Holland', 'Andrew Garfield', 'Tobey Magurie', 'Zendaya', 'Will Smith', 'Tom Cruise', 'Leonard DiCaprio', 'Ryan Reynolds', 'Chris Evans', 'Juice Wrld', 'Chris Pratt', 'Elon Musk', 'Jeff Bezoz', 'Kevin Hart', 'Drake', 'Lebron Jahames'
    stupidgoodmessageforbeg = 'Fine but you still owe me some money.', 'Ok but dont spend it that fast'

    earnings = random.randrange(101)

    await ctx.send(
        f"{random.choice(dummynames)} gave you {earnings} MetoCoins and they said: {random.choice(stupidgoodmessageforbeg)}"
    )

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users, f)


@client.command(aliases=(['with']))
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send(
            "You gotta enter an amount to withdraw silly :zany_face:")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("You don't have that much MetoCoins broke ass boy :rofl:")
        return
    if amount > bal[0]:
        await ctx.send("we just gonna ignore your attempt right there")
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, "bank")

    await ctx.send(f'You have withdrew {amount} MetoCoins from your bank')


@client.command(aliases=(['dep']))
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("You gotta enter an amount to deposit silly :zany_face:")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("You don't have that much MetoCoins broke ass boy :rofl:")
        return
    if amount > bal[0]:
        await ctx.send("we just gonna ignore your attempt right there")
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f'You have deposited {amount} MetoCoins from your bank')

@client.command(aliases=(['send']))
async def give(ctx, member:disnake.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount is None:
        await ctx.send("You gotta enter an amount to give silly :zany_face:")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("You don't have that much money broke ass boy :rofl:")
        return
    if amount > bal[0]:
        await ctx.send("we just gonna ignore your attempt right there")
        return

    await update_bank(ctx.author, -1 * amount, "bank")
    await update_bank(member, amount, "bank")

    await ctx.send(f'You gave {member.name} {amount} MetoCoins from your bank')


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal


keep_alive()
my_secret = os.environ['token']
client.run(my_secret)
