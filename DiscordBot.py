import discord
import requests
import random

client = discord.Client()

# List of 25 questions to determine if someone is a yandere or tsundere lover
questions = {
    'Do you prefer characters who are outgoing or reserved?': 'tsundere',
    'Do you like it when characters act possessive of their love interest?': 'yandere',
    'Do you enjoy characters who have a short temper?': 'tsundere',
    'Do you like it when characters are overly affectionate with their love interest?': 'yandere',
    'Do you enjoy characters who are sarcastic?': 'tsundere',
    'Do you like it when characters are overly jealous?': 'yandere',
    'Do you prefer characters who are independent or dependent?': 'tsundere',
    'Do you like it when characters are obsessive about their love interest?': 'yandere',
    'Do you enjoy characters who are cold and distant?': 'tsundere',
    'Do you like it when characters are possessive of their friends?': 'yandere',
    'Do you prefer characters who are straightforward or indirect?': 'tsundere',
    'Do you like it when characters are willing to do anything for their love interest?': 'yandere',
    'Do you enjoy characters who are teasing or playful?': 'tsundere',
    'Do you like it when characters are violent towards others who threaten their love interest?': 'yandere',
    'Do you prefer characters who are calm or emotional?': 'tsundere',
    'Do you like it when characters are willing to hurt others to protect their love interest?': 'yandere',
    'Do you enjoy characters who are flustered or embarrassed?': 'tsundere',
    'Do you like it when characters are willing to kill others who threaten their love interest?': 'yandere',
    'Do you prefer characters who are logical or impulsive?': 'tsundere',
    'Do you like it when characters are manipulative to protect their love interest?': 'yandere',
    'Do you enjoy characters who are blunt or tactful?': 'tsundere',
    'Do you like it when characters are willing to manipulate others to protect their love interest?': 'yandere',
    'Do you prefer characters who are serious or playful?': 'tsundere',
    'Do you like it when characters are willing to die for their love interest?': 'yandere',
    'Do you enjoy characters who are honest or deceitful?': 'tsundere',
    'Do you like it when characters are willing to go to extreme lengths to protect their love interest?': 'yandere'
}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('!animegif'):
        api_key = 'YOUR_API_KEY'
        query = 'anime'
        url = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit=50&offset=0&rating=g&lang=en'
        response = requests.get(url)
        data = response.json()
        gif = random.choice(data['data'])['images']['original']['url']
        await message.channel.send(gif)
    
    if message.content.startswith('!quiz'):
        scores = {'tsundere': 0, 'yandere': 0}
        
        for i in range(25):
            scores[random.choice(['tsundere', 'yandere'])] += 1
        
        tsundere_percentage = int(scores['tsundere'] / 25 * 100)
        yandere_percentage = int(scores['yandere'] / 25 * 100)

        await message.channel.send(f'Hello there, after I looked at your responses, I am shocked.\n\n- {yandere_percentage}% Yandere Lover\n- {tsundere_percentage}% Tsundere Lover\n\n*Wow, you\'re quite the interesting one, aren\'t you?*')
        
client.run('YOUR_DISCORD_BOT_TOKEN')


