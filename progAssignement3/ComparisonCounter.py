class ComparisonCounter:
    def __init__(self):
        self.counter = 0

    def set_value(self, value):
        self.counter = value

    def add_value(self, value):
        self.counter += value

    def get_value(self):
        return self.counter

