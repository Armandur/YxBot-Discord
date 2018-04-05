import discord
import sys

if sys.argv[1] == "DOCKERBUILD":
    sys.exit()

from YxBot import YxBot


bot = YxBot(discord.Client(), "!yxa")
bot.initAxeLibrary("data/yxtyp.txt", "data/yxfabrikat.txt")


@bot.client.event
async def on_ready():
    print('Logged in as')
    print(bot.client.user.name)
    print(bot.client.user.id)
    print('------')
    print("Invite url: " + discord.utils.oauth_url(bot.client.user.id))


@bot.client.event
async def on_message(message):
    await bot.handleMessage(message)

bot.client.run(sys.argv[1])
