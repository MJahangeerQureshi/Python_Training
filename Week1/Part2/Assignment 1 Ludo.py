import random

#Player True 0 piece was captured and returned back to the keep
#Player 2, Press enter to roll or type close to exit the program  (Fix tommorow)

def PositionUnsafe(num):
    '''
    Check if the space is safe for the piece
    '''
    if num == 1:
        return True
    else:
        if num % 5 == 0:
            return False
        else:
            return True

def RollDice():
    '''
    Random generator based upon probability distribution
    '''
    weighted_random = ['1'] * 25 +['2'] * 10 +['3'] * 10 +['4'] * 10 + ['5'] * 10 + ['6'] * 35
    roll_number = random.choice(weighted_random)
    print("Rolling dice .........",roll_number)
    return roll_number
    
class Player():
    '''
    Holds Player Identity
    '''
    def __init__(self, Player_num):
        self.Player_num = Player_num
    
    def SetPlayerNumber(self):
        return self.Player_num
        
    def SetPlayerNumber(self, Player_num):
        self.Player_num = Player_num
        
class Piece(Player):
    '''
    Holds Piece Number and the Piece Position
    '''
    def __init__(self, Piece_num, Piece_pos=-1):
        self.Piece_num = Piece_num
        self.Piece_pos = Piece_pos
        
    def GetPieceNumber(self):
        return self.Piece_num
    
    def SetPieceNumber(self, Piece_num):    
        self.Piece_num = Piece_num
        
    def GetPiecePosition(self):
        return self.Piece_pos
    
    def SetPiecePosition(self, Piece_pos):
        self.Piece_pos = Piece_pos
        
class Board():
    '''
    Holds Board Arrangement in a dictionary signifying piece postion and safe spaces
    along with methods for moving the player and handiling piece interaction
    '''
    def __init__(self, Piece_Arrangement={}):
        self.Piece_Arrangement = Piece_Arrangement
    
    def GetPieceArrangement(self):
        return self.Piece_Arrangement
    
    def SetPieceArrangement(self, Piece_Arrangement={}):
        self.Piece_Arrangement = Piece_Arrangement
        
    def DisplayPiecePositions(self, players):
        for player_number in range(len(players)):
            for piece_number in range(len(players[player_number])):
                print("Player",player_number+1,"Piece",piece_number+1,"is at position",
                      players[player_number][piece_number].GetPiecePosition(),"\n")
        
    def PlayerMovesOut(self, player_number, players):
        player = players[player_number]
        self.DisplayPiecePositions(players)
        
        while True:
            user_choice = input("Player "+str(player_number+1)+" which piece do you wish to move, 1 or 2 \n")
        
            if user_choice == "1" or user_choice == "2":
                piece_number = int(user_choice) - 1
                
                player[piece_number].GetPiecePosition()
                
                    
                
                player[piece_number].SetPiecePosition(1)
                break
            
            else:
                print("Invalid response choose 1 or 2")
        
    def PlayerMoves(self, player_number, players, roll_number):
        player = players[player_number]
        self.DisplayPiecePositions(players)
        
        while True:
            user_choice = input("Player "+str(player_number+1)+" which piece do you wish to move, 1 or 2 \n")
            if user_choice == "1" or user_choice == "2":
                piece_number = int(user_choice) - 1
                piece_initial_position = player[piece_number].GetPiecePosition()
                
                if piece_initial_position == -1 and roll_number != "6":
                    print("Sorry cant move that one select the other one")
                    continue
                    
                elif piece_initial_position == -1 and roll_number == "6":
                    print("Moving out a new piece")
                    piece_initial_position = player[piece_number].SetPiecePosition(1)
                    break
                
                else:
                    piece_new_position = piece_initial_position + int(roll_number)
                    player[piece_number].SetPiecePosition(piece_new_position)
                
                    other_player = players[not player_number]

                    if PositionUnsafe(piece_new_position):
                        for piece_number in range(len(other_player)):
                            if other_player[piece_number].GetPiecePosition() == piece_new_position:
                                print("Player",not player_number,piece_number,"piece was captured and returned back to the keep")
                                other_player[piece_number].SetPiecePosition(-1)
                            else:
                                pass
                    else:
                        pass   
                    break
            else:
                print("Invalid response choose 1 or 2")
            
        
class Ludo(Board):
    '''
    Helper functions holding the games logic
    '''
    def __init__(self):
        pass
    
    def PlayerHasntStarted(self,player):
        for piece in player:
            if piece.GetPiecePosition() != -1:
                return False
            else:
                pass
        return True
    
    def InitializePlayerValues(self):
        p1 = Piece(1)
        p1.SetPlayerNumber(1)
        p2 = Piece(2)
        p2.SetPlayerNumber(1)

        p3 = Piece(1)
        p3.SetPlayerNumber(2)
        p4 = Piece(2)
        p4.SetPlayerNumber(2)

        players = [[p1,p2],
                   [p3,p4]]
        
        return players

    def Run(self): 
        players = self.InitializePlayerValues()
        while True:
            for player_number in range(len(players)):
                while True:
                    user_response = input("Player "+str(player_number+1)+", Press enter to roll or type close to exit the program \n")
                    if user_response == '':

                        player = players[player_number]
                        roll_number = RollDice()
                        player_status = self.PlayerHasntStarted(player)

                        if player_status:
                            if roll_number == '6':
                                super().PlayerMovesOut(player_number, players)
                            else:
                                print("tough break, better luck next time")

                        else: # player has pieces
                            super().PlayerMoves(player_number, players,roll_number)
                        break

                    elif user_response == 'close':
                        return False

                    else:
                        print("Invalid, type close to exit the program")
                        pass

L = Ludo()
L.Run()