from .square import Square


class Property(Square):
    '''
    A base class for properties, which manages some common features
    of them.

    This include holding whether the property is owned (and if so, who by)
    and whether the property is mortgaged.

    Derived classes are: Street, Station, Utility.
    '''

    # A constant for an invalid player number, used to indicate
    # that the property is not owned...
    NOT_OWNED = -1

    class Set(object):
        '''
        An 'enum' for the different property sets.
        '''
        INVALID = 0
        BROWN = 1
        LIGHT_BLUE = 2
        PURPLE = 3
        ORANGE = 4
        RED = 5
        YELLOW = 6
        GREEN = 7
        DARK_BLUE = 8
        STATION = 9
        UTILITY = 10

    def __init__(self, name, street_set, price):
        '''
        The 'constructor'.
        '''
        super().__init__(name)

        # The set (BROWN, ORANGE etc)...
        self.street_set = street_set

        # The full price of the property.
        # The mortgage price is half of this price.
        self.price = price

        # True if the property is mortgaged...
        self.is_mortgaged = False

        # The player number of the owner...
        self.owner_player_number = Property.NOT_OWNED




