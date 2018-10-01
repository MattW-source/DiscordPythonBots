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


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")


@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == config["user_id"]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission")
    if message.content.upper().startswith('!AMIADMIN'):
        if config["role_id"] in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")
        

client.run(config["token"])
## In this case, you need to add the following to your config.json, right before the closing curly bracket (looks like this: } )
## "user_id": "ID of the discord user that you want to allow to run the !say command here",
## "role_id": "id of the role you want to set as an "administrator" role for use with the !amianadmin command
