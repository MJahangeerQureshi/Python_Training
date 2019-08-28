from include.player import Player

class Piece(object):
    '''
    Holds Piece Number and the Piece Position
    '''
    def __init__(self, Piece_num, Player, Piece_pos=-1):
        self.Piece_num = Piece_num
        self.Piece_pos = Piece_pos
        self.Player = Player 
        
    def get_piece_number(self):
        return self.Piece_num
    
    def set_piece_number(self, Piece_num):    
        self.Piece_num = Piece_num
        
    def get_piece_position(self):
        return self.Piece_pos
    
    def set_piece_position(self, Piece_pos):
        self.Piece_pos = Piece_pos
