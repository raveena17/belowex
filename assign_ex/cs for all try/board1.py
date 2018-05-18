class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range( H ):
            s += '|'   # add the spacer character
            for col in range( W ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*(W+1)+ '\n' + ' '
        for x in range(W):
            s += str(x%10) + ' '

        # add the bottom of the board
        # and the numbers underneath here
        
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ """
        H = self.height
        for row in range(H-1,-1,-1):
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                break

    def clear(self): 
        """ clears board"""
        H = self.height
        W = self.width
        for row in range(H):
            for col in range(W):
                self.delMove(col)


    def allowsMove( self, col ):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '
    

    def isFull( self ):
        """ returns True if the board is full """
        for col in range( self.width ):
            if self.allowsMove( col ):
                return False
        return True


    def delMove(self,c):
        """deletes top checker from column c"""
        H = self.height
        for row in range(H):
            #print row
            #print c
            #print self.data[row][c]
            if self.data[row][c] != ' ':
             #   print 'if'
                self.data[row][c] = ' '
                break
                

    def winsFor(self,ox):
        """checks if ox has won 4 in a row/col/diagonal"""
        # check for horizontal wins
        H = self.height
        W = self.width
        for row in range(0,H):
            for col in range(0,W-3):
                if self.data[row][col] == ox and \
                   self.data[row][col+1] == ox and \
                   self.data[row][col+2] == ox and \
                   self.data[row][col+3] == ox:
                    return True
        # check vertical
        for row in range(0,H-3):
            for col in range(0,W):
                if self.data[row][col] == ox and \
                   self.data[row+1][col] == ox and \
                   self.data[row+2][col] == ox and \
                   self.data[row+3][col] == ox:
                    return True
        #check southeast
        for row in range(0,H-3):
            for col in range(0,W-3):
                if self.data[row][col] == ox and \
                   self.data[row+1][col+1] == ox and \
                   self.data[row+2][col+2] == ox and \
                   self.data[row+3][col+3] == ox:
                    return True
        #check southwest
        for row in range(0,H-3):
            for col in range(W-4,W):
                if self.data[row][col] == ox and \
                   self.data[row+1][col-1] == ox and \
                   self.data[row+2][col-2] == ox and \
                   self.data[row+3][col-3] == ox:
                    return True
        return False

                    

    def hostGame(self):
        """hosts a full game of Connect Four"""
        print 'Welcome to Connect Four!' + '\n'
        print self
        while self.winsFor('O') == False and self.winsFor('X')== False and \
              self.isFull()==False:
            X = input("X's choice:")
            while self.allowsMove(X) == False:
                print 'Try again!'
                X = input("X's choice:")
            if self.allowsMove(X) == True and self.isFull() == False:
                self.addMove(X,'X')
                print b
            if self.winsFor('X') == True:
                print b
                print "X wins -- Congratulations!"
                break
            if self.isFull() == True:
                print b
                print "Game over! Tie!"
                break
            O = input("O's choice:")
            while self.allowsMove(O) == False:
                print 'Try again!'
                O = input("O's choice:")
            if self.allowsMove(O) and self.isFull() == False:
                self.addMove(O,'O')
                print b
            if self.winsFor('O') == True:
                print b
                print "O wins -- Congratulations!"
                break
            if self.isFull() == True:
                print b
                print "Game over! Tie!"
                break
        return
