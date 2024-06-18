import discord
from discord.ext import commands
import program
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.command()
async def haslo(ctx, lenght = 8):
    await ctx.send(program.gen_pass(lenght))

@bot.command()
async def photos_show(ctx):
    nazwy = os.listdir('memes')
    randomowy_obrazek = random.choice(nazwy)
    with open ('memes/' + randomowy_obrazek, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run()
