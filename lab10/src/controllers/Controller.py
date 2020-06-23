from models.FuzzySystem import FuzzySystem


class Controller:
    def __init__(self, texture, capacity, cycle_type, rules):
        self.system = FuzzySystem(rules)
        self.system.add_description('texture', texture)
        self.system.add_description('capacity', capacity)
        self.system.add_description('cycle_type', cycle_type, out=True)

    def compute(self, inputs):
        return "If we have the capacity: " + str(inputs['capacity']) + \
               " and texture: " + str(inputs['texture']) + \
               ", we'll probably have the operating cycle_type: " + \
               str(self.system.compute(inputs))
