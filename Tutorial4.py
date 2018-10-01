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

Client = discord.Client()
client = commands.Bot(command_prefix = config["prefix"])

chat_filter = config["chat_filter"]
bypass_list = config["bypass_list"]

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
                   
                    
        

client.run(config["token"])
## Here you need to remove the 2 keys added to our config from Tutorial 3
## and add these 2:
## "chat_filter": ["array", "of", "words", "to", "block", "seperated", "just", "like", "this"],
## "bypass_list": ["array", "of", "discord", "user", "ids", "that", "dont", "get", "their", "message", "deleted", "when", "they", "use", "a", "banned", "word", "123456789012345678"]