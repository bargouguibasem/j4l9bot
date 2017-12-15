import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asynico
import time

Client = discord.Client()
client = commands.Bot (command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

client.run("MzkwMTg1MjU2NjEyOTIxMzU1.DRGfPQ.371uRap_0Ehl4WDAWuGBHyOi8fc")
