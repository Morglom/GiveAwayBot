import os, discord, datetime, time
from discord.ext import commands
from dotenv import load_dotenv
import giveaway

description = 'A bot for handling giveaways'

# Dictionary for storing the ids of the management and announcement channels in the first two positions and the list of giveaways in the third position for each server
guildDict = {}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', description=description)

@bot.command()
@bot.event
async def on_ready():
    print(f'{bot.user} is connected')

# When bot joins a server it creates a management role, a management channel and an announcement channel for giveaways
bot.run(TOKEN)