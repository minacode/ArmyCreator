class Warrior:
    def __init__(self, name, points, has_bow, army, count = 1):
        self.name = name
        self.points = points
        self.has_bow = bool(has_bow)
        self.army = army
        self.count = count
        self.options = set()
        self.foreign_options = set()

    @staticmethod
    def from_database(data):
        return Warrior(*data)

    def __str__(self):
        return self.name + ' | ' + str(self.points) + ' | ' + str(self.has_bow) + ' | ' + self.army

    def __repr__(self):
        return str(self)

    def get_points_for_single(self):
        p = self.points
        p += sum((o.get_points() for o in self.options))
        p += sum((o.get_points() for o in self.foreign_options))
        return p

    def get_points(self):
        return self.get_points_for_single() * self.count

    def add_option(self, option):
        self.options.add(option)

    def add_foreign_option(self, option):
        self.foreign_options.add(option)
