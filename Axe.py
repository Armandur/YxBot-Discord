class Axe:
    def __init__(self, type, make):
        self.type = type
        self.make = make

    def __str__(self):
        return "En " + self.type + " tillverkad av " + self.make