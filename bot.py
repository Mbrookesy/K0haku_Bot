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

@bot.command()
async def calc(ctx, operation, arg1, arg2):
    arg1 = int(arg1)
    arg2 = int(arg2)
    if operation == "add":
        await ctx.send(arg1 + arg2)
    elif operation == "sub":
        await ctx.send(arg1 - arg2)
    elif operation == "mul":
        await ctx.send(arg1 * arg2)
    elif operation == "div":
        await ctx.send(arg1 / arg2)
    else:
        await ctx.send("Invalid Operation")

bot.run(token)
