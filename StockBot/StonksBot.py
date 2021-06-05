import os

from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws
    await ws.send_privmsg(os.environ['CHANNEL'], f"{os.environ['BOT_NICK']} has landed")


if __name__ == "__main__":
    bot.run()
