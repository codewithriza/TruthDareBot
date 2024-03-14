import os
from dotenv import load_dotenv
import discord
import random
from discord.ext import commands
from discord.ui import Button, View
from truthordarechoices import truths, dares

# Load environment variables from .env file
load_dotenv()

# Get the Discord bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a bot instance
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())


@bot.command(name='tod', help='Starts a game of Truth or Dare')
async def truth_or_dare(ctx):
    # Create an embed with welcome message and buttons
    embed = discord.Embed(title="Welcome to Truth or Dare!", description="Are you ready to play this game?", color=0x00ff00)
    view = View()
    view.add_item(Button(label="Truth", custom_id="truth"))
    view.add_item(Button(label="Dare", custom_id="dare"))
    await ctx.send(embed=embed, view=view)

@bot.event
async def on_button_click(interaction):
    # Check if the button clicked is for truth or dare
    if interaction.custom_id == "truth":
        question = random.choice(truths)
    elif interaction.custom_id == "dare":
        question = random.choice(dares)
    else:
        return

    # Create an embed with the random question
    embed = discord.Embed(title="Truth or Dare", description=question, color=0xff0000)
    await interaction.response.edit_message(embed=embed, view=None)

# Run the bot
bot.run(TOKEN)
