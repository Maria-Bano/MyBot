import discord
import requests
import json
from dotenv import load_dotenv
import os


def get_meme():
    response = requests.get('https://meme-api.com/gimme?count=1')  # Force single meme
    json_data = json.loads(response.text)
    # The API sometimes returns a list if count>1, but now it's guaranteed single
    return json_data['url'] if 'url' in json_data else json_data['memes'][0]['url']


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.strip().lower() == '$meme':  # Safer matching
            meme_url = get_meme()
            await message.channel.send(meme_url)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
load_dotenv()
client.run(os.environ['DISCORD_TOKEN'])
