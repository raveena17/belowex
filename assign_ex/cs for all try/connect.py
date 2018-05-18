'''class Player(p):
    """ an AI player for Connect Four """
    p=player('X','Left',3)
    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s'''
import random

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """returns opposite player's playing piece"""
        if self.ox == "O":
            return "X"
        elif self.ox == "X":
            return "O"
        else:
            return "Error."
        
    def scoreBoard(self,b):
        """returns float of score of input b(Board); 100.0 if win for self,
        0.0 if loss for self, 50.0 otherwise"""
        opp = self.oppCh()
        if b.winsFor(self.ox) == True:
            return 100.0
        elif b.winsFor(opp) == True:
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self,scores):
        """input scores: nonempty list of floats(List)
        returns column number of highest score; if tie:
        returns column number of best score using tbt method"""

        maxIndices = []
        mx = max(scores)
        for x in range(len(scores)):
            if mx == scores[x]:
                maxIndices += [x]
        #return maxIndices
        if len(maxIndices) == 1:
            return maxIndices[0]
        else:
            if self.tbt == "RIGHT":
                return maxIndices[len(maxIndices)-1]
            elif self.tbt == "LEFT":
                return maxIndices[0]
            elif self.tbt == "RANDOM":
                c = random.choice(range(len(maxIndices)))
                return maxIndices[c]

    def scoresFor(self,b):
        """returns list of scores for moving into each possible column"""

        opp = self.oppCh()
        scores = [50]*b.width
        for col in range(b.width):
            if b.winsFor(self.ox) == True:
                scores[col] = 100.0
            elif b.winsFor(self.oppCh()) == True:
                scores[col] = 0.0
            elif b.allowsMove(col) == False:
                scores[col] = -1.0
            elif self.ply == 0:
                scores[col] = self.scoreBoard(b)
            else:
                b.addMove(col,self.ox)
                opp = Player(self.oppCh(),self.tbt,self.ply-1)
                s = opp.scoresFor(b)
                scores[col] = (100 - max(s))
                b.delMove(col)
        return scores


    def nextMove(self,b):
        """returns column number (int) that Player chooses to move to; input b: object of type Board"""
        return self.tiebreakMove(self.scoresFor(b))
    
