import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='#')

#on ready event

@bot.event
async def on_ready():
    print ("Hands up!  Ready to bet!")
    print (bot.user.name)
    print (bot.user.id)

#Make the bot run - insert discord authentication token
#bot.run("token")