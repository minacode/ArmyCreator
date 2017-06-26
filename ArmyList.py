class ArmyList:
    def __init__(self):
        self.warbands = []

    def add_warband(self, wb):
        self.warbands.append(wb)

    def remove_warband(self, wb):
        self.warbands.remove(wb)

    def get_warbands(self):
        return self.warbands
        
    def get_points(self):
        return sum((w.get_points() for w in self.warbands))

    def get_all_heroes(self):
        return [w.hero for w in self.get_warbands()]
