import os
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Client(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)


client = Client()
client.run(os.environ["DISCORD_TOKEN"])
