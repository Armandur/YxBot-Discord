import discord
import random
import asyncio


paths = list()
paths.append("data/yxfabrikat.txt")
paths.append("data/yxtyp.txt")
paths.append("data/kroppsdel.txt")

sets = [set(), set(), set()]

i = 0
for path in paths:
    f = open(path)
    for l in f:
        if l not in sets[i]:
            sets[i].add(l.strip('\n'))
    f.close()
    i += 1

yxfabrikat = sets[0]
yxtyp = sets[1]
kroppsdel = sets[2]

print("-- Fabrikat --")
print(yxfabrikat)
print("-- Typer --")
print(yxtyp)
print("-- Kroppsdelar --")
print(kroppsdel)


def yxa():
    print("-- Yxar --")
    fab = random.sample(yxfabrikat, 1)[0]
    typ = random.sample(yxtyp, 1)[0]
    krp = random.sample(kroppsdel, 1)[0]

    return "YxBot tar en " + typ + " tillverkad av " + fab + " och hugger den i " + krp + " på {}.\n"

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("Invite url: " + discord.utils.oauth_url(client.user.id))


@client.event
async def on_message(message):
    if message.content.startswith('!yxa'):
        tmp = await client.send_message(message.channel, 'Letar reda på en yxa...')

        m = message.content[5:]

        await client.edit_message(tmp, yxa().format(m))

client.run(TOKEN)