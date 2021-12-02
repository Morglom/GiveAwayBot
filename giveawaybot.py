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
async def create(ctx):
    "Create a new giveaway"

@bot.command()
async def announce(ctx):
    "Announce a created giveaway, making the giveaway public and creating a post in the giveaway channel that can be used to sign up for the giveaway"

@bot.command()
async def update(ctx):
    "Update the details of a giveaway"

@bot.command()
async def info(ctx):
    "Get the details of the giveaway"

@bot.command()
async def list(ctx):
    "Lists upcoming giveaways in this server"
    
@bot.event
async def on_ready():
    print(f'{bot.user} is connected')

# When bot joins a server it creates a management role, a management channel and an announcement channel for giveaways
@bot.event
async def on_guild_join(self, guild)
        # Check if the role already exists and if not create it
        manager_role = get(ctx.guild.roles, name="Giveaway Manager")
        if manager_role is None
            manager_role = await guild.create_role(name="Giveaway Manager")
        
        # Overwrites to limit access to the management channel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            manager_role: discord.PermissionOverwrite(read_messages=True)
        }
        
        # Check if channels exist and if not create them
        if get(guild.text_channels, name='giveaway-management') is None:
            await guild.create_text_channel("giveaway-management", overwrites = overwrites)
        if get(guild.text_channels, name='giveaways') is None:
            await guild.create_text_channel("giveaways")
        
        # Add details of the guild to the dictionary
        channelDict[guild.id] = [ get(guild.text_channels, name='giveaway-management').id , get(guild.text_channels, name='giveaways').id , []]
    
bot.run(TOKEN)