from ...game import Board
from ...squares import Property, Street
import logging
import tkinter as tk


class MessagingServer(object):
    '''
    TODO: Kyle
    '''

    def __init__(self, update_every_n_turns, sleep_between_turns_seconds):
        '''
        The 'constructor'.
        '''
        self.logger = logging.getLogger(__name__)
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=200, height=200)
        # canvas.create_rectangle(10, 10, 190, 190, fill="red")
        self.canvas.create_text(100, 100, text='Hello World')
        self.canvas.pack()
        self.window.update()

    def send_start_of_tournament_message(self, players):
        '''
        Sends the start-of-tournament message.

        'players' is a list of (player-name, player-number)
        '''
        self.logger.warning('send_start_of_tournament_message')
        self.logger.warning(players)

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
        owner = game.state.board.squares[1].owner
        if owner is not None:
            self.logger.warning(owner.name)
            self.canvas.delete('all')
            self.canvas.create_text(100, 100, text=owner.name)
            self.canvas.pack()
            self.window.update()
