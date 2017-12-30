from handlers.AxingHandler import AxingHandler

from Axe import Axe

class YxBot:

    def __init__(self, client, keyword):
        self.client = client
        self._init_handlers()

        self.axeLibrary = set()
        self.entities = {}

        self.axesAndUsers = {}

        self.keyword = keyword

    def _init_handlers(self):
        self.handlers = [
            AxingHandler(self)
        ]

    async def handleMessage(self, message):
        for handler in self.handlers:
            await handler.handle_message(message)

    def initAxeLibrary(self, pathType, pathMake):
        paths = [pathType, pathMake]
        sets = [set(), set()]

        i = 0
        for path in paths:
            f = open(path)
            for l in f:
                if l not in sets[i]:
                    sets[i].add(l.strip('\n'))
            f.close()
            i += 1

        for _type in sets[0]:
            for make in sets[1]:
                self.axeLibrary.add(Axe(_type, make))
