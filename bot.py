import discord
import random


BOT_USERNAME = "@Gork"
TOKEN_FILE_NAME = "token.txt"
ACCEPTED_PHRASES = [
    "is this real?",
    "is this true?",
    "confirm?",
]
RESPONSES = [
    # positive
    "it is certain", "it is decidedly so", "without a doubt", "yes definitely",
    "you may rely on it", "as i see it, yes", "most likely", "outlook good",
    "yes", "signs point to yes",

    # neutral
    "reply hazy, try again", "ask again later", "better not tell you now",
    "cannot predict now", "concentrate and ask again",

    # negative
    "don't count on it", "my reply is no", "my sources say no",
    "outlook not so good", "very doubtful",
]


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

random.seed()


@client.event
async def on_ready():
    print("bot ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.clean_content
    # if the msg starts with the bot username and is more than just the bot's username
    if content.startswith(BOT_USERNAME) and len(content) > len(BOT_USERNAME)+1:
        phrase = content[len(BOT_USERNAME):].strip()
        # if the phrase matches any accepted phrase
        if any(x.lower() == phrase.lower() for x in ACCEPTED_PHRASES):
            idx = random.randint(0, len(RESPONSES))
            await message.channel.send(RESPONSES[idx])

token_file = open(TOKEN_FILE_NAME)
token = token_file.read().strip()
token_file.close()

client.run(token)
