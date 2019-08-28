from include.board import Board

class Ludo(object):
    def __init__(self):
        self.board = Board() 

    def Run(self):
        '''
        The run function starts the game until the user says otherwise
        '''
        number_of_players = 2
        results = True
        while results:
            for player_number in range(number_of_players):
                results = self.board.play_turn(player_number)
        print("Game terminated\n")      