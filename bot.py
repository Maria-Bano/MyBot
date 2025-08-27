import discord
import requests
import json
from dotenv import load_dotenv
import os

def get_meme():
    response = requests.get('https://meme-api.com/gimme/1')  
    json_data = json.loads(response.text)
    
    if 'memes' in json_data and len(json_data['memes']) > 0:
        meme_url = json_data['memes'][0]['url']
        return meme_url
    else:
        return json_data.get('url', 'No meme found')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.strip().lower() == '$meme':
            meme_url = get_meme()
            await message.channel.send(meme_url)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
