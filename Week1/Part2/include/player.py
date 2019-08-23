class Player():
    '''
    Holds Player Identity
    '''
    def __init__(self, Player_num):
        self.Player_num = Player_num
    
    def get_player_number(self):
        return self.Player_num
        
    def set_player_number(self, Player_num):
        self.Player_num = Player_num
        
class Piece(Player):
    '''
    Holds Piece Number and the Piece Position
    '''
    def __init__(self, Piece_num, Player_num, Piece_pos=-1):
        self.Piece_num = Piece_num
        self.Piece_pos = Piece_pos
        super().set_player_number(Player_num)
        
    def get_piece_number(self):
        return self.Piece_num
    
    def set_piece_number(self, Piece_num):    
        self.Piece_num = Piece_num
        
    def get_piece_position(self):
        return self.Piece_pos
    
    def set_piece_position(self, Piece_pos):
        self.Piece_pos = Piece_pos
