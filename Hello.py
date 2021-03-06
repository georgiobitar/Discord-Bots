import discord
import os
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv(config.api_token))
