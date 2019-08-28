import random
from include.player import Player
from include.piece import Piece

class Board(object):
    def __init__(self, players=None):
        p1 = Piece(1,Player(1))
        p2 = Piece(2,Player(1))
        p3 = Piece(1,Player(2))
        p4 = Piece(2,Player(2))

        self.players = [[p1,p2], [p3,p4]]

    def roll_dice(self):
        '''
        Random generator based upon probability distribution
        '''
        weighted_random = ['1'] * 25 +['2'] * 10 +['3'] * 10 +['4'] * 10 + ['5'] * 10 + ['6'] * 35
        roll_number = random.choice(weighted_random)
        print("Rolling dice ......... "+roll_number+"\n")
        return roll_number

    def position_unsafe(self, position):
        '''
        Check if the space is safe for the piece
        Spaces that are multiples of 5 are safe
        '''
        if position == 1:
            return True
        else:
            if position % 5 == 0:
                return False
            else:
                return True

    def player_still_in_keep(self, player):
        '''
        Returns a boolean value signifying if the player has started the game or not
        '''
        for piece in player:
            if piece.get_piece_position() != -1:
                return False
        return True

    def alter_board(self, ludo_board, piece_position, piece_name, overlap=False):
        if overlap:
            if piece_name == "A":
                return ludo_board.replace(piece_name, piece_name.lower()).replace("_A", "AB")
            elif piece_name == "B":
                return ludo_board.replace(piece_name, piece_name.lower()).replace("_B", "AB")
            elif piece_name == "C":
                return ludo_board.replace(piece_name, piece_name.lower()).replace("_C", "CD")
            else:
                return ludo_board.replace(piece_name, piece_name.lower()).replace("_D", "CD")
        else:
            board_position = f'{int(piece_position%46):02d}'
            return ludo_board.replace(piece_name, piece_name.lower()).replace(board_position, "_"+piece_name)

    def show_board(self, players):
        '''
        Displays the Board.
        '''
        ludo_board = '''
                        23|24                   
                        22|25                   
                        21|26                   
                        20|27                   
                        19|28                   
                        18|29                   
      13  14  15   16   17|30  31  32   33   34
      12------------------|-------------------35
      11  10  09   08   07|40  39  38   37   36
                        06|41                   
                        05|42                   
         1.A   2.B      04|43    1.C    2.D       
                        03|44                   
                        02|45                   
                        01|00                   

        '''
        for player_number in range(len(players)):
            for piece_number in range(len(players[player_number])):
                piece_position = players[player_number][piece_number].get_piece_position()
                
                if player_number == 0 and piece_number == 0:
                    if piece_position != -1:
                        overlap = players[0][1].get_piece_position == piece_position
                        ludo_board = self.alter_board(ludo_board, piece_position, 'A', overlap)
                elif player_number == 0 and piece_number == 1:
                    if piece_position != -1:
                        overlap = players[0][0].get_piece_position == piece_position
                        ludo_board = self.alter_board(ludo_board, piece_position, 'B', overlap)
                elif player_number == 1 and piece_number == 0:
                    if piece_position != -1:
                        overlap = players[1][1].get_piece_position == piece_position
                        ludo_board = self.alter_board(ludo_board, piece_position, 'C', overlap)
                else:
                    if piece_position != -1:
                        overlap = players[1][0].get_piece_position == piece_position
                        ludo_board = self.alter_board(ludo_board, piece_position, 'D', overlap)

        print(ludo_board)    

    def play_turn(self, player_number):
        '''
        A player turn is computed over here including the dice roll as 
        well as multiple turns in the case of a luck 6 roll
        '''
        repeat_turn = True
        
        while repeat_turn:
            user_input = input('Player '+str(player_number+1)+' press enter to roll\n')
            if user_input == "":
                roll = self.roll_dice()
                if roll !='6' and self.player_still_in_keep(self.players[player_number]):
                    print('tough luck\n')
                    break
                else:
                    repeat_turn = self.move_player_piece(player_number, self.players, roll)
                    if roll != '6':
                        repeat_turn = False
            elif user_input == 'close':
                return False
            else:
                print('invalid entry, type "close" if you wish to leave\n')      
        return True

    def move_player_piece(self, player_number, players, roll):
        '''
        A helper function specially move the piece in response to a dice roll
        '''
        self.show_board(players)

        while True:
            user_input = input('Player '+str(player_number+1)+' which piece do you want to move 1 or 2\n')
            if user_input == '1' or user_input == '2':
                piece_number = int(user_input) - 1
                piece_initial_position = players[player_number][piece_number].get_piece_position()
                if piece_initial_position == -1:
                    if roll == '6':
                        print('Moving out a new piece :)')
                        if player_number == 0:
                            players[player_number][piece_number].set_piece_position(1)
                        else:
                            players[player_number][piece_number].set_piece_position(36)
                        return False
                    else:
                        print('Cant do that, that piece is still in the keep\n')
                else:
                    initial_position = players[player_number][piece_number].get_piece_position()
                    new_position = initial_position + int(roll)
                    players[player_number][piece_number].set_piece_position(new_position)

                    self.check_if_any_piece_captured(player_number, players, new_position)
                    return True
            else:
                print('Invalid entry, choose either 1 or 2\n')

    def check_if_any_piece_captured(self, player_number, players, new_position):
        '''
        This functions verifies if 2 opposing pieces occupy the same space
        if so the player with the presiding piece is returned to the keep
        '''
        for piece_number in range(len(players[1 - player_number])):
            if new_position == players[1 - player_number][piece_number].get_piece_position() and self.position_unsafe(new_position):
                print("Player "+str((1 - player_number)+1)+"s, piece "+str(piece_number+1)+" was captured and returned to the keep\n")
                players[1 - player_number][piece_number].set_piece_position(-1)