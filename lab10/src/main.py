from controllers.Controller import Controller
from models.FuzzyDescription import FuzzyDescription
from models.FuzzyRule import FuzzyRule

""" The washing machine """


def run():
    texture = FuzzyDescription()
    capacity = FuzzyDescription()
    cycle_type = FuzzyDescription()

    rules = []

    texture.add_region('very soft', trap_region(-10, 0.0, 0.4, 0.8))
    texture.add_region('soft', tri_region(0.4, 0.8, 1.2))
    texture.add_region('normal', tri_region(0.5, 1.0, 1.5))
    texture.add_region('resistant', trap_region(0.9, 1.1, 1.2, 10))

    capacity.add_region('small', trap_region(-1500, 0, 1, 2))
    capacity.add_region('medium', tri_region(1, 4.5, 8))
    capacity.add_region('high', trap_region(5, 6, 7, 1500))

    cycle_type.add_region('delicate', trap_region(-150, 0, 0.4, 0.8), inverse_line(0.8, 0.4))
    cycle_type.add_region('easy', tri_region(0.5, 0.7, 1.0), inverse_tri(0.5, 0.7, 1.0))
    cycle_type.add_region('normal', tri_region(0.6, 0.7, 1.1), inverse_tri(0.6, 0.7, 1.1))
    cycle_type.add_region('intense', trap_region(1.2, 1.4, 1.5, 1500), inverse_line(1.2, 1.4))

    rules.append(FuzzyRule({'texture': 'very soft', 'capacity': 'small'},
                           {'cycle_type': 'delicate'}))
    rules.append(FuzzyRule({'texture': 'soft', 'capacity': 'small'},
                           {'cycle_type': 'easy'}))
    rules.append(FuzzyRule({'texture': 'normal', 'capacity': 'small'},
                           {'cycle_type': 'easy'}))
    rules.append(FuzzyRule({'texture': 'resistant', 'capacity': 'small'},
                           {'cycle_type': 'easy'}))

    rules.append(FuzzyRule({'texture': 'very soft', 'capacity': 'medium'},
                           {'cycle_type': 'easy'}))
    rules.append(FuzzyRule({'texture': 'soft', 'capacity': 'medium'},
                           {'cycle_type': 'normal'}))
    rules.append(FuzzyRule({'texture': 'normal', 'capacity': 'medium'},
                           {'cycle_type': 'normal'}))
    rules.append(FuzzyRule({'texture': 'resistant', 'capacity': 'medium'},
                           {'cycle_type': 'normal'}))

    rules.append(FuzzyRule({'texture': 'very soft', 'capacity': 'high'},
                           {'cycle_type': 'normal'}))
    rules.append(FuzzyRule({'texture': 'soft', 'capacity': 'high'},
                           {'cycle_type': 'normal'}))
    rules.append(FuzzyRule({'texture': 'normal', 'capacity': 'high'},
                           {'cycle_type': 'intense'}))
    rules.append(FuzzyRule({'texture': 'resistant', 'capacity': 'high'},
                           {'cycle_type': 'intense'}))

    controller = Controller(texture, capacity, cycle_type, rules)

    print(controller.compute({'capacity': 7, 'texture': 0.5}))
    print(controller.compute({'capacity': 3, 'texture': 0.8}))
    print(controller.compute({'capacity': 1, 'texture': 0.4}))
    print(controller.compute({'capacity': 7, 'texture': 0.3}))


def trap_region(a, b, c, d):
    """
        Returns a higher order function for a trapezoidal fuzzy region
    """
    return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))


def tri_region(a, b, c):
    """
        Returns a higher order function for a triangular fuzzy region
    """
    return trap_region(a, b, b, c)


def inverse_line(a, b):
    return lambda val: val * (b - a) + a


def inverse_tri(a, b, c):
    return lambda val: (inverse_line(a, b)(val) + inverse_line(c, b)(val)) / 2


if __name__ == '__main__':
    run()
