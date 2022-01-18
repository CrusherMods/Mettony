#RENAME THE FILE TO BOT.PY
import disnake
from disnake.ext import commands
import os
import json
import random
import time
import urllib
import asyncio

client = commands.Bot(command_prefix="<")
client.remove_command("help")
client.sniped_messages = {}

owner = 731616848860282901

@client.command()
async def ping(ctx):
  embed = disnake.Embed(title = 'Pong! 🏓', description = f'Latency: {round(client.latency * 1000)}ms', color = disnake.Colour.blue())
  await ctx.send(embed=embed)

@client.event
async def on_ready():
    await client.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.playing, name=f"with your dad"))
    print(f"Logged in as {client.user}!\nyour gay")

@client.event
async def on_message_delete(message):
  if message.author.id == owner:
    print(f"======================================\nMettony Owner message's are deleted!\nMessage: {message.content}\nChannel: #{message.channel.name}\nTime: {message.created_at}\n======================================")
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

# METERS
@client.command()
async def gaymeter(ctx, *, user=None):
 if user is None:
  embed = disnake.Embed(title=f"Gay Meter", description=f"You are {random.randrange(100)}% gay.", color=disnake.Colour.blue())
  await ctx.send(embed=embed)
 else:
  embed = disnake.Embed(title=f"Gay Meter", description=f"{user} is {random.randrange(100)}% gay.", color=disnake.Colour.blue())
  await ctx.send(embed=embed)

@client.command()
async def coolmeter(ctx, *, user=None):
 if user is None:
  embed = disnake.Embed(title=f"Cool Meter", description=f"You are {random.randrange(100)}% cool.", color=disnake.Colour.blue())
  await ctx.send(embed=embed)
 else:
  embed = disnake.Embed(title=f"Cool Meter", description=f"{user} is {random.randrange(100)}% cool.", color=disnake.Colour.blue())
  await ctx.send(embed=embed)

#WE ARE DOING SOME TROLLING TODAY BOIS
@client.command()
async def say(ctx, *, say=None):
  await ctx.channel.purge(limit=1)
  await ctx.send(f"{say}")

@client.command()
async def invite(ctx):
  await ctx.send('https://discord.com/api/oauth2/authorize?client_id=842098192778264576&permissions=8&scope=bot%20applications.commands')

@client.command()
async def credits(ctx):
  embed = disnake.Embed(title=f"Credits for Mettony", description=f"Owner: CrusherNotDrip#0001\nHelp with Coding: Hafimie\nCommand Ideas: NeonFurious", color=disnake.Colour.blue())
  await ctx.send(embed=embed)
  print(f"used funny credits command")

@client.command()
async def sauce(ctx):
  await ctx.send('https://github.com/CrusherMods/Mettony')
  print(f"User used Github command to eat Spagetti")

client.run("YOUR_TOKEN_HERE")
