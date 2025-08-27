import discord
import requests
import json
from dotenv import load_dotenv
import os

def get_meme():
    response = requests.get('https://meme-api.com/gimme?count=1')
    json_data = json.loads(response.text)
    return json_data['url'], json_data['title']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.strip().lower() == '$meme':
            meme_url, meme_title = get_meme()
            embed = discord.Embed(title=meme_title, color=discord.Color.random())
            embed.set_image(url=meme_url)
            await message.channel.send(embed=embed)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
