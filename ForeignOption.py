from Option import Option


class ForeignOption(Option):
    def __init__(self, giving_unit, receiving_unit, name, points, is_bow):
        Option.__init__(self, receiving_unit, name, points, is_bow)
        self.giving_unit = giving_unit


