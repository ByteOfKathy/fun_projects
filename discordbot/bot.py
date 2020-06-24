import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
f = open('secret.txt', 'r')
token = f.readline().strip()
person = f.readline().strip()
# genius = f.readline().strip()
f.close()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord!')

@client.event
async def on_message(message):
    if str(message.author) is person:
        # '<:ekans:615520951706189845>',
        areactions= ['🇵', '🇾', '🇹', '🇭', '🇴', '🇳', '🐍']
        for reaction in areactions:
            await message.add_reaction(reaction)

    # if str(message.author) in genius:
    #     breactions = ['🇬', '🇪', '🇳', '🇮', '🇺', '🇸', '💡']
    #     for reaction in breactions:
    #         await message.add_reaction(reaction)

client.run(token)