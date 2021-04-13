import discord
import random
from discord.ext import commands
from random import randint

bottoken = open("token.txt", "r")
bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="; prefix"))
  print("bot ready")

@bot.command()
async def ask(ctx, question):
  answer = randint(1, 5)
  if answer == 1:
    await ctx.send("I'll say YES!")
  if answer == 2:
    await ctx.send("I'm not really sure, sorry.")
  if answer == 3:
    await ctx.send("Isn't that impossible?")
  if answer == 4:
    await ctx.send("I have to say yes for now...")
  if answer == 5:
    await ctx.send("It's a big fat NO for me.")

@bot.command()
async def ask_tts(ctx, question):
  answer = randint(1, 5)
  if answer == 1:
    await ctx.send("you should!", tts = True)
  if answer == 2:
    await ctx.send("not really sure about that...", tts = True)
  if answer == 3:
    await ctx.send("No! How ridiculous", tts = True)
  if answer == 4:
    await ctx.send("I have to say yes for now...", tts = True)
  if answer == 5:
    await ctx.send("It's a No for me...", tts = True)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.MissingRequiredArgument):
    await ctx.send("You didn't provide any answers.")

bot.run(bottoken.read())