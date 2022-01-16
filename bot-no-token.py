import lightbulb
import hikari

bot = lightbulb.BotApp(
    token='TOKEN_GOES_HERE', 
    default_enabled_guilds=(924006119788138586, 896023046983397436, 891837711823036446))

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('mettony is gonna fuck your dad') #true

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong! ||im gonna fuck you later||') #It was too basic so now mettony is gonna fuck you

@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'This is a sub command')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
   await ctx.respond('THIS TUTORIAL IS WORKING') #BUT I GOTTA WAIT A WEEK

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2) #9 + 10 = 21 STUPID

bot.run()
