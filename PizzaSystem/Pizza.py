class Pizza:
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Klasik(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.name="Margarita"
        self.description="Normal kalınlıkta malzemesiz sade hamur"
        self.cost=50

class Margarita(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.name="Margarita"
        self.description="Domatesli kaşarlı bir taban"
        self.cost=60

class Ince(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.name="Margarita"
        self.description="İncecik bir taban"
        self.cost=70

