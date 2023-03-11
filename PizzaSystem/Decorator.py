class Decorator:
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Zeytin(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.name="Zeytin"
        self.description="Gemlik Zeytini"
        self.cost=10


class Mantar(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.name="Mantar"
        self.description="Taze mantar"
        self.cost=20


class Sogan(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.name="Soğan"
        self.description="Karamelize Soğan"
        self.cost=30

