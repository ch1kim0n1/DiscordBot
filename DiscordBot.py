import discord
import random

client = discord.Client()

# List of music recommendations
music_list = ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip Hop', 'Country']

# List of anime genres
anime_genres = ['Action', 'Comedy', 'Romance', 'Fantasy', 'Drama', 'Mystery/Thriller', 'Historical', 'Sci-Fi', 'Horror', 'Real-Life']

# Dictionary of anime survey questions and corresponding anime genres
anime_questions = {
    'Do you prefer action-packed anime?': 'Action',
    'Do you enjoy comedies in anime?': 'Comedy',
    'Would you rather watch a romance anime?': 'Romance',
    'Do you like anime that has a lot of fantasy elements?': 'Fantasy',
    'Do you prefer a more serious, drama-filled anime?': 'Drama',
    'Would you enjoy a mystery or thriller anime?': 'Mystery/Thriller',
    'Do you like anime that is set in the past?': 'Historical',
    'Do you like anime that is set in the future?': 'Sci-Fi',
    'Would you watch a horror anime?': 'Horror',
    'Do you like anime that is based on real-life events?': 'Real-Life'
}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!music'):
        music_recommendation = random.choice(music_list)
        await message.channel.send(f'Here is a music recommendation: {music_recommendation}')

    elif message.content.startswith('!manga'):
        manga_page = random.randint(1, 150)
        await message.channel.send(f'Why not read page {manga_page} of your manga today?')

    elif message.content.startswith('!anime'):
        await message.channel.send('Let\'s determine what genre of anime you should watch. Answer the following questions with either "yes" or "no".')
        
        user_preferences = {}
        for question in anime_questions:
            response = await client.wait_for('message', check=lambda m: m.author == message.author and (m.content.lower() == 'yes' or m.content.lower() == 'no'))
            user_preferences[anime_questions[question]] = (1 if response.content.lower() == 'yes' else 0)
        
        recommended_genre = max(user_preferences, key=user_preferences.get)
        await message.channel.send(f'Based on your answers, it looks like you might enjoy watching anime in the {recommended_genre} genre.')

client.run('YOUR_BOT_TOKEN_HERE')


