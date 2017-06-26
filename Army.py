

class Army:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def from_database(data):
        return Army(*data)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
