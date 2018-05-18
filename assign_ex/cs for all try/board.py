class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.a=0
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        
        # and the numbers underneath here
        
        return s       # the board is complete, return it
    
    def addmove(self,col,ox):
           H=self.height
           for row in range(H-1,-1,-1):
               if self.data[row][col]==' ':
                   self.data[row][col]=ox
                   break
    def allowmove(self,col):
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col]== ' '
    def isfull(self):
        for col in range(self.width):
            if self.allowmove(col):
                return False
        return True
    def delmove(self,c):
        for row in range(self.height):
            if self.data[row][c]!=' ':
                self.data[row][c]=' '
                break
    def winsfor(self,ox):
        H=self.height
        W=self.width
        for row in range(0,H):
            for col in range(0,W-3):
                if self.data[row][col]==ox and \
                   self.data[row][col+1]==ox and \
                   self.data[row][col]==ox and \
                   self.data[row][col+3]==ox:
                   return True
        for row in range(0,H-3):
            for col in range(0,W):
                if self.data[row][col]==ox and \
                   self.data[row+1][col]==ox and \
                   self.data[row+2][col]==ox and \
                   self.data[row+3][col]==ox:
                   return True
        for row in range(0,H-3):
            for col in range(0,W-3):
                if self.data[row][col]==ox and \
                   self.data[row+1][col+1]==ox and \
                   self.data[row+2][col+2]==ox and \
                   self.data[row+3][col+3]==ox:
                   return True
        for row in range(0,H-3):
            for col in range(W-4,W):
                if self.data[row][col]==ox and \
                   self.data[row+1][col+1]==ox and \
                   self.data[row+2][col+2]==ox and \
                   self.data[row+3][col+3]==ox:
                    return True
                   
        return False 
    def hostgame(self):
        print 'Welcome to connect four'
        print self
        while self.winsfor('O')==False and self.winsfor('X')==False and  \
              self.isfull()==False:
            X=input('X s choice:')
            while self.allowmove(X)==False:
                print 'try again'
                X=input('X s choice:')
            if self.allowmove(X)==True and self.isfull()==False:
                    self.addmove(X,'X')
                    print b
            if self.winsfor('X')==True:
                    print b
                    print "X wins -- congratulation"
                    break
            if self.isfull()==True:
                    print b
                    print "Game over tie"
                    break
            O=input("O choice:")
            while self.allowmove(O)==False:
                   print 'try again'
                   X=input('O s choice:')
            if self.allowmove(O) == True and self.isfull() == False:
                       self.addmove(O,'O')
                       print b
            if self.winsfor('O')==True:
                       print b
                       print "O wins -- congratulation"
                       break
            if self.isfull() == True:
                       print b
                       print "Game over tie"
                       break
        return
                            
                


        
        
    


