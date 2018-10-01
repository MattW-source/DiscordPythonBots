import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json

# Function to load the config.json file
def load_json():
	# Open the config.json file and store it as the variable configFile.
	with open("config.json") as configFile:
		# Use the .load method from the json library to load the config file and return a object we can use in code to get config values.
		return json.load(configFile)

config = load_config() # Because the method above doesn't store the returned object in a variable, we need to do that.

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = config["prefix"]) #Initialise client bot, get prefix from config file.


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"

# Remember kids, never ever commit your token to a public repository! Always use config files!
client.run(config["token"])

###
# An Example of what the config.json should look like
###
# {
#   "token": "insert your bot token into this string",
#   "prefix": "insert your desired prefix into this string"
# }