import discord
import random

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

client = discord.Client(intents=intents)

anime_library = ['Action', 'Comedy', 'Drama', 'Romance', 'Fantasy', 'Mystery', 'Horror', 'Thriller', 'Adventure']
music_library = ['Rock', 'Pop', 'Jazz', 'Classical', 'Rap', 'Hip Hop', 'Blues', 'Metal', 'Country']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!music'):
        music = random.choice(music_library)
        await message.channel.send(f'How about some {music} music?')

    elif message.content.startswith('!anime'):
        anime = random.choice(anime_library)
        await message.channel.send(f'You should check out some {anime} anime!')

    elif message.content.startswith('!randomM'):
        page = random.randint(1, 100)
        await message.channel.send(f'How about opening a random manga page? How about page {page}?')

    elif message.content.startswith('!help'):
        await message.channel.send('Commands:\n!music - recommends a random music genre\n!anime - recommends a random anime genre\n!randomM - suggests opening a random manga page\n!help - shows this help message')

    else:
        await message.channel.send('Error: Invalid command. Type !help for a list of available commands.')

client.run('MTA3NDE3MzE0Nzg3Nzc0ODgwNg.Gkgq9D.GfsfR3bUIPUog7bjuR0MyJWFIHkXYMoV_RDmJM')

