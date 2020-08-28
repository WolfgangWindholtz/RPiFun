arr =[]
import Tictactoe
Tic = Tictactoe.Tictactoe()

    
 
while True:

    x = (input("enter n for new game , q to quit \n"))
    if(x == "n"):
        while True:
            b = input(" enter x to place x or o to place o, q to quit ")
            if(b == "x"):
                row = int(input("what row? "))
                col = int(input("what col? "))
                Tic.placePeice("x",row,col)
            elif(b == "o"):
                row = int(input("what row? "))
                col = int(input("what col? "))  
                Tic.placePeice("o",row,col)
            elif(b == "q"):
                print("you quit")
                break
            else:
                print("invalid input")

            Tic.printArr()
            #showBoard(Tic)

            if(Tic.checkWin("x")):
                print(" x won! good job")
            if(Tic.checkWin("o")):
                print(" o won! good job")
    
    elif(x == "q"):
        break

    else:
        print("invalid input")