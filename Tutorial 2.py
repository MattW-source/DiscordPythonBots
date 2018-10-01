import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json # Import the json library to load our config

# Function to load the config.json file
def load_json():
	# Open the config.json file and store it as the variable configFile.
	with open("config.json") as configFile:
		# Use the .load method from the json library to load the config file and return a object we can use in code to get config values.
		return json.load(configFile)

config = load_config() # Because the method above doesn't store the returned object in a variable, we need to do that.

Client = discord.Client()
client = commands.Bot(command_prefix = config["prefix"])


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")


@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    

client.run(config["token"]) # Load token from config, and connect to Discord with it.
