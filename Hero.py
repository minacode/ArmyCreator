class Hero:
    def __init__(self, name, points, can_lead, army):
        self.name = name
        self.points = points
        self.can_lead = bool(can_lead)
        self.army = army
        self.options = set()

    @staticmethod
    def from_database(data):
        return Hero(*data)

    def __str__(self):
        return self.name + ' | ' + str(self.points) + ' | ' + str(self.can_lead) + ' | ' + self.army

    def __repr__(self):
        return str(self)

    def get_points(self):
        return self.points + sum((o.get_points() for o in self.options))

    def add_option(self, option):
        self.options.add(option)
