class Tictactoe:
   
    def __init__(self):
        self.board = [ [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.p = ' '
        


    def printArr(self):
        row =  3
        for row in range(row):
             
                print(self.board[row])

    def place(self,row,col):
        self.board[row][col] = self.p
    
    def placePeice(self, peice, row ,col):
        self.board[row][col] = peice
    
    def clearBoard(self):
        row,col = 3,3
        for row in range(row):
            for col in range(col):
                placePeice(self,' ',row,col)

    def checkWin(self, p):
        row,col = 3,3
        ret = False
        for row in range(3):
            isRow = True
            isColumn = True
            for col in range(3):
                if(self.board[row][col] != p):
                    isRow = False

                
                if(self.board[col][row] != p):
                    isColumn = False
                
             
            if(isColumn or isRow):
                ret = True
                break

        if( self.board[0][0] == p and 
            self.board[1][1] == p and
            self.board[2][2] == p 
        ):
            ret = True
              

        if( self.board[0][2] == p and 
            self.board[1][1] == p and
            self.board[2][0] == p
        ):
                ret = True
            
        return ret    
            
               
                 

    
