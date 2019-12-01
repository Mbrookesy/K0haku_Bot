import discord
from discord.ext import commands

token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='K!')


@bot.event  # event decorator/wrapper
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {bot.user}')  # notification of login.


@bot.command()
async def hello(ctx):
    await ctx.send("...Hello")

@bot.command()
async def copycat(ctx, *args):
    await ctx.send('{}'.format(' '.join(args)))

bot.run(token)
