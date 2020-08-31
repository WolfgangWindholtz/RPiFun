# Import all files from 
# tkinter and overwrite 
# all the tkinter files 
# by tkinter.ttk 
from tkinter import *
from tkinter.ttk import *
import Tictactoe

Tic = Tictactoe.Tictactoe()

peice = ' '

  
# function to be called when 
# keyboard buttons are pressed 
def show(event): 
    Tic.printArr()

def place1(event): 
    Tic.place(0,0)
def place2(event): 
    Tic.place(1,0)
def place3(event): 
    Tic.place(2,0)
def place4(event): 
    Tic.place(0,1)
def place5(event): 
    Tic.place(1,1)
def place6(event): 
    Tic.place(2,1)
def place7(event): 
    Tic.place(0,2)
def place8(event): 
    Tic.place(1,2)
def place9(event): 
    Tic.place(2,2) 

def setX(event):
    Tic.p = 'x'
def setO(event):
    Tic.p = 'o'       



# creates tkinter window or root window 
root = Tk() 
root.geometry('400x200') 

#buttons for board 
quitButton = Button( text='Quit',
            command=quit)
showButton = Button(text= 'show')

setXButton = Button(text = 'place x')
setOButton = Button(text = 'place o')

Button1 = Button()
Button2 = Button()
Button3 = Button()
Button4 = Button()
Button5 = Button()
Button6 = Button()
Button7 = Button()
Button8 = Button()
Button9 = Button()




Button1.grid(column = 1 ,row = 0 )   
Button2.grid(column = 1 ,row = 1 )
Button3.grid(column = 1 ,row = 2 )
Button4.grid(column = 2 ,row = 0 )
Button5.grid(column = 2 ,row = 1 )
Button6.grid(column = 2 ,row = 2 )
Button7.grid(column = 3 ,row = 0 )
Button8.grid(column = 3 ,row = 1 )
Button9.grid(column = 3 ,row = 2 )
quitButton.grid(column = 0 ,row = 0 )
showButton.grid(column = 0 , row = 1)
setXButton.grid(column = 2, row = 4)
setOButton.grid(column = 3, row = 4)
  

showButton.bind("<Button>",  show) 
setOButton.bind("<Button>", setO)
setXButton.bind("<Button>", setX)

Button1.bind("<Button>",  place1) 
Button2.bind("<Button>",  place2) 
Button3.bind("<Button>",  place3) 
Button4.bind("<Button>",  place4) 
Button5.bind("<Button>",  place5) 
Button6.bind("<Button>",  place6) 
Button7.bind("<Button>",  place7) 
Button8.bind("<Button>",  place8) 
Button9.bind("<Button>",  place9) 


  
mainloop()

