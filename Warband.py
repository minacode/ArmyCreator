class Warband:
    def __init__(self, army_list):
        self.army_list = army_list
        self.hero = None
        self.warriors = []

    def add_warrior(self, w):
        self.warriors.append(w)

    def set_hero(self, h):
        self.hero = h

    def remove_warrior(self, warrior):
        try:
            self.warriors.remove(warrior)
        except:
            print('could not remove', warrior)

    def get_warrior_count(self):
        return sum((w.count for w in self.warriors))

    def get_points(self):
        warrior_points = sum((w.get_points() for w in self.warriors))
        if self.hero is None:
            return warrior_points
        else:
            return warrior_points + self.hero.get_points()

    def remove_all_warriors(self):
        self.warriors = []
        
    def get_fill_fraction(self):
        if self.hero is None:
            return 0.0
        elif self.hero.can_lead:
            return (1 + self.get_warrior_count()) / 13
        else:
            return 1.0
