class MyClass:
    """A simple example class"""

    def __init__(self):
        self.board = [ [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


    def printArr(self):
        row =  3
        for row in range(row):
             
                print(self.board[row])

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
        for row in range(row):
            isRow = True
            isColumn = True
            for col in range(col):
                if(self.board[row][col] != p):
                    isRow = False

                
                if(self.board[row][col] != p):
                    isColumn = False
                
             
            if(isColumn or isRow):
                ret = True
                break
            if( self.board[row][col] == p and 
                self.board[row][col] == p and
                self.board[row][col] == p 
             ):
                ret = True; 
              

            if( self.board[row][col] == p and 
                self.board[row][col] == p and
                self.board[row][col] == p
            ):
                    ret = True; 
            
        return ret    
            
               
                 

    
x = MyClass()
x.placePeice('x',1,1)
x.placePeice('x',1,0)
x.placePeice('x',1,2)
print(x.checkWin('x'))
x.printArr()