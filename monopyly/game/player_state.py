import copy
from ..squares import Street


class PlayerState(object):
    '''
    Holds data for one player, such as the amount of money that have and
    which properties they own.

    Note: The player algorithm is not in this class (or in a derived class).
    '''

    def __init__(self, player_number):
        '''
        The 'constructor'.
        '''

        # The square the player is currently on (0 = Go, 39 = Mayfair etc).
        # This can be used as an index into the squares property of the board...
        self.square = 0

        # The amount of money owned by the player...
        self.cash = 1500

        # The collection of properties owned by the player.
        # This is held as a set of integers, each of which is an index
        # to one of the squares on the board. The squares themselves hold
        # information about how many houses are on them, whether they are
        # mortgages and so on...
        self.property_indexes = set()

        # How many Get Out Of Jail Free cards the player is holding...
        self.number_of_get_out_of_jail_free_cards = 0

        # The player number. Each player is assigned a number when the
        # game starts, and this is reported to the player AI. This can help
        # an AI know which player is themself when looking at the state of
        # the game.
        #
        # This is a zero-based number, which can be used as an index into
        # the GameState.players list to find the corresponding Player object.
        self.player_number = player_number

        # Whether the player is in jail, and if so how many turns they
        # have been there...
        self.in_jail = False
        self.number_of_turns_in_jail = 0

        # The collection of complete sets owned by this player.
        # The items in the collection are Property.Set 'enums'.
        # TODO: Fill this in when ownership of properties changes.
        self.sets_owned = set()

    def copy(self):
        '''
        Returns a copy of the player state.
        '''
        return copy.deepcopy(self)

    def get_number_of_houses_and_hotels(self, board):
        '''
        Returns the number of houses and hotels owned by this player.
        '''
        number_of_houses = 0
        number_of_hotels = 0
        for index in self.property_indexes:
            # We find the square for this index and check if
            # it is a street (ie, not a station or utility)...
            square = board.get_square_by_index(index)
            if(type(square) != Street):
                continue

            number_of_houses += property.number_of_houses
            number_of_hotels += (1 if property.has_hotel else 0)

        return number_of_houses, number_of_hotels




