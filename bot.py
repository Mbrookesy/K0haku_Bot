import discord
from discord.ext import commands
import time
import asyncio

token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='K!')

joined = 0
messages = 0

async def update_stats():
    await bot.wait_until_ready()
    global messages, joined

    while not bot.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)

@bot.event  # event decorator/wrapper
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {bot.user}')  # notification of login.

@bot.event
async def on_member_join(member):
    global joined
    joined += 1

@bot.event
async def on_message(message):
    global messages
    messages += 1
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("...Hello")

@bot.command()
async def copycat(ctx, *args):
    await ctx.send('{}'.format(' '.join(args)))

@bot.command()
async def calc(ctx, operation, arg1: int, arg2: int):
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

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@bot.command()
async def users(ctx):
    for i in bot.users:
        await ctx.send(i)

bot.loop.create_task(update_stats())

bot.run(token)
