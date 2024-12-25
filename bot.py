import os
import discord
from dotenv import load_dotenv


class Client(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)


load_dotenv()

client = Client()
client.run(os.environ["TOKEN"])
