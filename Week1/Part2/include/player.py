class Player(object):
    '''
    Holds Player Identity
    '''
    def __init__(self, Player_num):
        self.Player_num = Player_num
        
    def get_player_number(self):
        return self.Player_num
        
    def set_player_number(self, Player_num):
        self.Player_num = Player_num