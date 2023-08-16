from ...game import Board
from ...squares import Property, Street
import logging


class MessagingServer(object):
    '''
    TODO: Kyle
    '''

    def __init__(self, update_every_n_turns, sleep_between_turns_seconds):
        '''
        The 'constructor'.
        '''
        self.logger = logging.getLogger(__name__)

    def send_start_of_tournament_message(self, players):
        '''
        Sends the start-of-tournament message.

        'players' is a list of (player-name, player-number)
        '''
        self.logger.warning('send_start_of_tournament_message')

    def send_start_of_game_message(self):
        '''
        Sends a message to the GUI saying that a game is about to start.
        '''
        self.logger.warning('send_start_of_game_message')

    def send_end_of_turn_messages(self, tournament, game, force_send):
        '''
        Called at the end of each turn.
        We send a player-info update and a board update.
        '''
        self.logger.warning('send_end_of_turn_messages')
