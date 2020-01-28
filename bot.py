import discord
from discord.ext import commands
import time
import asyncio
import random
import datetime
from datetime import datetime
from itertools import cycle

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
                realtime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(int(time.time())))
                f.write(f"Time: {realtime}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(60)
        except Exception as e:
            print(e)
            await asyncio.sleep(60)

@bot.event  # event decorator/wrapper
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {bot.user}')  # notification of login.

status = ['with Eliel', 'Tetris', 'with random buttons']

async def change_status():
    await bot.wait_until_ready()
    statuses = cycle(status)

    while bot.is_closed:
        current_status = next(statuses)
        await bot.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(60)

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

@bot.command()
async def age(ctx):
    t1 = datetime.utcfromtimestamp(1420675200)
    t2 = datetime.now() - t1
    await ctx.send("I am currently " + str(t2.days) + " days old")

@bot.command()
async def message(ctx, user: discord.User, *message):
    message = str(message)
    message = message.replace("(", "")
    message = message.replace(")", "")
    message = message.replace("'", "")
    message = message.replace(",", " ")

    await user.send(message)
    await ctx.send("Message Sent")

@bot.command()
async def elielfact(ctx):
    f = open("eliel_facts.txt", "r")
    lines = f.readlines()
    fact = random.randint(0, 5)
    if fact == 0:
        await ctx.send(lines[0])
    elif fact == 1:
        await ctx.send(lines[1])
    elif fact == 2:
        await ctx.send(lines[2])
    elif fact == 3:
        await ctx.send(lines[3])
    elif fact == 4:
        await ctx.send(lines[4])

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Beep Boop command not found")
    else:
        raise error


bot.loop.create_task(update_stats())
bot.loop.create_task(change_status())

bot.run(token)
