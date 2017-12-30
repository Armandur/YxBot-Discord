from anytree import NodeMixin


class Bodypart(NodeMixin):
    def __init__(self, parent, enett, side, name, essential=False, health=3):
        self.parent = parent
        self.enett = enett
        self.side = side
        self.name = name
        self.essential = essential
        self.health = health # 3 = Oskadad, 2 = Blåslagen, 1 = Blodig, 0 = Avkapad

    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def state(self):
        _str = {3: "oskada", 2: "blåslage", 1: "blodig", 0: "avkapa"}

        append = ""

        if self.enett == "En":
            append = "d"
        elif self.enett == "Ett":
            append = "t"

        if self.health == 2:
            if self.enett == "En":
                append = "n"
        elif self.health == 1:
            if self.enett == "En":
                append = ""
            elif self.enett == "Ett":
                append = "t"

        return _str[self.health] + append

    def __str__(self):
        if self.side:
            return self.enett + " " + self.state() + " " + self.side + self.name
        else:
            return self.enett + " " + self.state() + " " + self.name