from random import randrange


def roll_dice():
    '''
    Random generator based upon probability distribution
    '''
    weighted_random = ['1'] * 25 +['2'] * 10 +['3'] * 10 +['4'] * 10 + ['5'] * 10 + ['6'] * 35
    return random.choice(weighted_random)
    
class Player():
    '''
    Holds Player Identity
    '''
    def __init__(self, Player_num):
        self.Player_num = Player_num
    
    def get_Player_num(self):
        return self.Player_num
        
    def set_Player_num(self, Player_num):
        self.Player_num = Player_num
        
class Piece(Player):
    '''
    Holds Piece Number and the Piece Position
    '''
    def __init__(self, Piece_num, Piece_pos):
        self.Piece_num = Piece_num
        self.Piece_pos = Piece_pos
        
    def get_Piece_num(self):
        return self.Piece_num
    
    def set_Piece_num(self, Piece_num):    
        self.Piece_num = Piece_num
        
    def get_Piece_pos(self):
        return self.Piece_pos
    
    def set_Piece_pos(self, Piece_pos):
        self.Piece_pos = Piece_pos
        
class Board():
    '''
    Holds Board Arrangement in a dictionary signifying piece postion and safe spaces
    '''
    def __init__(self, Piece_Arrangement):
        self.Piece_Arrangement = Piece_Arrangement
    
    def get_Piece_Arrangement(self):
        return self.Piece_Arrangement
    
    def set_Piece_Arrangement(self, Piece_Arrangement):
        self.Piece_Arrangement = Piece_Arrangement

class Ludo(Board):
    '''
    Helper functions holding the games logic
    '''
    def __init__(self):
        pass
    
    def run_game(self):
        print("Welcome to this small ludo game, type 1 to start the game and type 0 to exit the program")
        while True:
            user_input = input("Input:    ")
            if user_input == "0":
                print("Exiting Program")
                break
            elif user_input == "1":
                self.Display()
            else:
                print("Invalid entry type 0 to exit the program")
