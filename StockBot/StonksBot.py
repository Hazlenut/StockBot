import os
from twitchio.ext import commands

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    name=os.environ['BOT_NAME'],
    prefix=os.environ['BOT_PREFIX'],
    channels=[os.environ['CHANNEL']]
)



if __name__ == "__main__":
    bot.run()