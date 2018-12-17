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

@bot.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await bot.send_message(message.channel, 'Calculating messages...')
        async for log in bot.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await bot.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await bot.send_message(message.channel, 'Done sleeping')


#creating betting class
class Bet:
  def __init__(self, betting, user, amount):
    self.betting = True
    self.user = user.name
    self.amount = int

#Make the bot run - insert discord authentication token
#bot.run("token")