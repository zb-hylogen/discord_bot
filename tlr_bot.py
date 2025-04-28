import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import random
import asyncio
from collections import deque

from keep_alive import keep_alive
from modules.db_wrapper import db_wrapper

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced_commands = await bot.tree.sync()
        #await bot.sync_commands()
        print(f"{bot.user} is online!")
    except Exception as e:
        print("An error with synching commands has occurred", e)


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


#lookup prefix commands

# @bot.event
# async def on_message(msg):
#     if msg.author.id != bot.user.id:
#         await msg.channel.send(f"Interesting Message, {msg.author.mention}")

@bot.tree.command(name="greet", description="Sends a greeting to the user")
async def greet(interaction: discord.Interaction):
    username = interaction.user.mention
    await interaction.response.send_message(f"Hello there, {username}")

#num_dice="The number of dice to roll.", num_sides="The number of sides on each die."
@bot.tree.command(name="roll", description="roll (n) dice with (x) sides" )
async def roll(interaction: discord.Interaction, num_dice:int=1, num_sides:int=6):
    results = []
    for x in range(num_dice):
        results.append(str(random.randrange(1, num_sides)))
    #username = interaction.user.mention

    msg = f"Rolling ({num_dice}) d({num_sides})"
    res = ','.join(results)
    s = sum(map(int, results))
    await interaction.response.send_message(f"{msg}: [{res}] Total:{s}")




query = "SELECT * FROM first_table"
wrapper = db_wrapper(query)
result = wrapper.execute(query)
for row in result:
    print(row)


load()
bot.run(TOKEN)

# async def main():
#     query = "SELECT * FROM first_table"
#     wrapper = db_wrapper(query)
#     result = await wrapper.execute(query)
#     for row in result:
#         print(row)
# load()
# bot.start(TOKEN)


    



# asyncio.run(main())





