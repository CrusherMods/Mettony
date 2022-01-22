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
  await client.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"Amogus on Netflix"))
  await asyncio.sleep(4)
  await client.change_presence(status=disnake.Status.do_not_disturb, activity=disnake.Activity(type=disnake.ActivityType.playing, name=f"your dad"))
  await asyncio.sleep(4)
  await client.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.playing, name=f"amogus fidget toy"))
  await asyncio.sleep(4)
  await client.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.listening, name=f"1 hour amogus drip"))
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

    embed = disnake.Embed(title=f"Command Cooldown", description=f"Spamming isn't cool, {cooldowntext}.",color=disnake.Color.blue())
    await ctx.send(embed=embed)

@client.event
async def on_message_delete(message):
  if message.author.id == owner:
    print(f"======================================\nAuthor message's are deleted!\nMessage: {message.content}\nChannel: #{message.channel.name}\nTime: {message.created_at}\n======================================")
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
  else:
    print(f"======================================\n{message.author} message's are deleted!\nMessage: {message.content}\nChannel: #{message.channel.name}\nTime: {message.created_at}\n======================================")
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command(aliases=['s', 'deletedmessage', 'delm'])
async def snipe(ctx):
  contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
  embed = disnake.Embed(description=contents, color=disnake.Color.blue(), timestamp=time)
  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.display_avatar.url)
  embed.set_footer(text=f"Deleted in: #{channel_name}")
  await ctx.channel.send(embed=embed)

@client.command()
async def say(ctx, *, say=None):
  await ctx.channel.purge(limit=1)
  await ctx.send(f"{say}")

@client.command()
async def coolm(ctx, *, user=None):
 if user is None:
  embed = disnake.Embed(title=f"Cool Meter 😎", description=f"You are {random.randrange(100)}% cool.", color=disnake.Colour.blue())
  await ctx.send(embed=embed)
 else:
  embed = disnake.Embed(title=f"Cool Meter 😎", description=f"{user} is {random.randrange(100)}% cool.", color=disnake.Colour.blue())
  await ctx.send(embed=embed)

@client.command()
async def slap(ctx, member:disnake.Member=None):
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

  await ctx.send(file = disnake.File('assets/slapping.jpg'))

  os.remove("assets/slapping.jpg")

@client.command()
async def help(ctx):
  embed = disnake.Embed(title=f"Help Command", description=f"**Information:**\n \nm!credits - Shows the Credits of Mettony\n\n**Utilitys:**\n\nm!snipe - Shows the Latest Deleted Message", color=disnake.Colour.blue())
  embed.set_footer(text="Prefixes are: m!, mettony & susbot but we use m! for an example")
  await ctx.send(embed=embed)

@client.command()
async def credits(ctx):
  embed = disnake.Embed(title=f"Credits", description="Owner: CrusherNotDrip#0001\nCo-Owner: Hafimie#8182", color=disnake.Colour.blue())
  await ctx.send(embed=embed)

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)
