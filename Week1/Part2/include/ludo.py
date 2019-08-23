import random
from include.player import Piece, Player

class Board():
    def __init__(self):
        pass

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
        Spaces that ere multiples of 5 are safe
        '''
        if position == 1:
            return True
        else:
            if position % 5 == 0:
                return False
            else:
                return True

    def player_still_in_keep(self, player):
        for piece in player:
            if piece.get_piece_position() != -1:
                return False
            else:
                pass
        return True

    def show_board(self, players):
        '''
        Display the condition of the Board.
        '''
        for player_number in range(len(players)):
            for piece_number in range(len(players[player_number])):
                position = players[player_number][piece_number].get_piece_position()
                if position == -1:
                    print("              Player",player_number+1,"Piece",piece_number+1,"is at position : Keep\n")
                else:
                    print("              Player",player_number+1,"Piece",piece_number+1,"is at position : ",position,"\n")    

    def play_turn(self, player_number, players):
        repeat_turn = True
        
        while repeat_turn:
            
            user_input = input('Player '+str(player_number+1)+' press enter to roll\n')
            
            if user_input == "":
                roll = self.roll_dice()

                if roll !='6' and self.player_still_in_keep(players[player_number]):
                    print('tough luck\n')
                    break
                
                else:
                    repeat_turn = self.move_player_piece(player_number, players, roll)

                    if roll == '6':
                        pass
                    else:
                        repeat_turn = False
                        

            elif user_input == 'close':
                return False

            else:
                print('invalid entry, type "close" if you wish to leave\n')      
        
        return True

    def move_player_piece(self, player_number, players, roll):
        self.show_board(players)

        while True:
            user_input = input('Player '+str(player_number+1)+' which piece do you want to move 1 or 2\n')
            
            if user_input == '1' or user_input == '2':
                piece_number = int(user_input) - 1
                piece_initial_position = players[player_number][piece_number].get_piece_position()
            
                if piece_initial_position == -1:
                    if roll == '6':
                        print('Moving out a new piece :)')
                        players[player_number][piece_number].set_piece_position(1)
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
        for piece_number in range(len(players[1 - player_number])):
            if new_position == players[1 - player_number][piece_number].get_piece_position() and self.position_unsafe(new_position):
                print("Player "+str((1 - player_number)+1)+"s, piece "+str(piece_number+1)+" was captured and returned to the keep\n")
                players[1 - player_number][piece_number].set_piece_position(-1)
            else:
                pass



class Ludo(Board):
    def __init__(self):
        pass

    def initialize_players(self):
        p1 = Piece(1,1)
        p2 = Piece(2,1)
        p3 = Piece(1,2)
        p4 = Piece(2,2)

        players = [[p1,p2],
                   [p3,p4]]
        
        return players

    def Run(self):
        players = self.initialize_players()
        results = True
        while results:
            for player_number in range(len(players)):
                results = super().play_turn(player_number, players)
        print("Game terminated\n")