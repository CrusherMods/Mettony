import hikari

bot = hikari.GatewayBot(token='TOKEN_GOES_HERE')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('mettony is gonna fuck your dad')

bot.run()
