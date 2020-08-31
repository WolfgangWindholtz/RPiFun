# Import all files from 
# tkinter and overwrite 
# all the tkinter files 
# by tkinter.ttk 
from tkinter import *
from tkinter.ttk import *
import time
import board
import neopixel
import Tictactoe


pixel_pin = board.D18
num_pixels = 40
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)



Tic = Tictactoe.Tictactoe()

peice = ' '


def showBoard( Tac):
    row , col = 3,3
    i = 11
    for row in range(3):
            for col in range(3):
                if(Tac.board[row][col] == 'x'):
                    pixels[i] = (100,0,0)

                elif(Tac.board[row][col] == 'o'):
                    pixels[i] = (0,100,0)

                else:
                    pixels[i] = (50,50,50)

                i = i + 1      

            i = i+5
    pixels.show()
    time.sleep(1)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)



def clear4():
    
    Tic.clearBoard()
    
    for i in range(num_pixels):
        
        pixels[i] = (0,0,0)
    pixels.show()

# function to be called when 
# keyboard buttons are pressed 
def clear(event): 
    Tic.printArr()
    clear4()
    pixels.show()


def place1(event): 
    Tic.place(0,0)
    showBoard(Tic)
    pixels.show()
def place2(event): 
    Tic.place(1,0)
    showBoard(Tic)
    pixels.show()

def place3(event): 
    Tic.place(2,0)
    showBoard(Tic)
    pixels.show()
def place4(event): 
    Tic.place(0,1)
    showBoard(Tic)
    pixels.show()
def place5(event): 
    Tic.place(1,1)
    showBoard(Tic)
    pixels.show()
def place6(event): 
    Tic.place(2,1)
    showBoard(Tic)
    pixels.show()
def place7(event): 
    Tic.place(0,2)
    showBoard(Tic)
    pixels.show()
def place8(event): 
    Tic.place(1,2)
    showBoard(Tic)
    pixels.show()
def place9(event): 
    Tic.place(2,2)
    showBoard(Tic)
    pixels.show() 

def setX(event):
    Tic.p = 'x'
    showBoard(Tic)
    pixels.show()
def setO(event):
    Tic.p = 'o'
    showBoard(Tic)
    pixels.show()       



# creates tkinter window or root window 
root = Tk() 
root.geometry('400x200') 

#buttons for board 
quitButton = Button( text='Quit',
            command=quit)
clearButton = Button(text= 'clear')

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
clearButton.grid(column = 0 , row = 1)
setXButton.grid(column = 2, row = 4)
setOButton.grid(column = 3, row = 4)
  

clearButton.bind("<Button>", clear) 
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

