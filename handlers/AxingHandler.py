from handlers.MessageHandler import MessageHandler
from Body import Body
from anytree import RenderTree
import random


class AxingHandler(MessageHandler):

    async def handle_message(self, message):
        if message.content.startswith(self.bot.keyword + " ") and len(message.content) > 4:
            tmp = await self.bot.client.send_message(message.channel, "Letar reda på " + message.author.mention +"s yxa...")

            if message.author not in self.bot.axesAndUsers:
                self.bot.axesAndUsers[message.author] = random.choice(tuple(self.bot.axeLibrary))

            axe = self.bot.axesAndUsers[message.author]

            ent = message.content[5:]

            if ent not in self.bot.entities:
                self.bot.entities[ent] = Body()

            outMessage = ""

            if len(self.bot.entities[ent].bodyparts.descendants) > 0:
                target = random.choice(self.bot.entities[ent].bodyparts.descendants)
            else:
                target = self.bot.entities.bodyparts

            intensity = random.randint(1, 3)

            if self.bot.entities[ent].alive is False:
                intensity = 3

            outMessage += "YxBot tar " + str(axe)[0].lower() + str(axe)[1:]

            if intensity == 1:
                 outMessage += " och skär med den i " + target.enett[0].lower() + target.enett[1:]
            elif intensity == 2:
                outMessage += " och slår med den i " + target.enett[0].lower() + target.enett[1:]
            elif intensity == 3:
                outMessage += " och hugger med den i " + target.enett[0].lower() + target.enett[1:]

            outMessage += " "

            if target.side is not None:
                outMessage += target.side

            outMessage += target.name + " på "

            if self.bot.entities[ent].alive is False:
                outMessage += "den redan avlidne "

            outMessage += ent + "."

            target.damage(intensity)

            outMessage += "\n" + ent + "s " + target.name + " blev " + target.state() + " av attacken!"

            if target.health == 0:
                target.parent = None

                if target.essential:
                    self.bot.entities[ent].alive = False

                for bodypart in target.descendants:
                    if bodypart.essential:
                        self.bot.entities[ent].alive = False

                if self.bot.entities[ent].alive is False:
                    outMessage += "\n" + ent + " är död!"

            print(outMessage)
            for pre, fill, node in RenderTree(self.bot.entities[ent].bodyparts):
                print("%s%s" % (pre, node))

            await self.bot.client.edit_message(tmp, outMessage)
