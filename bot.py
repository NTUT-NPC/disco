import os
import discord


class Client(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)


client = Client()
client.run(os.environ["DISCORD_TOKEN"])
