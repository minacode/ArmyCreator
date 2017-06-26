class Option:
    def __init__(self, unit, name, points, is_bow):
        self.unit = unit
        self.name = name
        self.points = points
        self.is_bow = is_bow
        self.is_set = False

    @classmethod
    def from_database(cls, data):
        return cls(*data)
        
    def toggle_set(self):
        self.is_set = not self.is_set

    def get_points(self):
        return self.points * int(self.is_set)
