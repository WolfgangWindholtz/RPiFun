# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import Tictactoe



# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 40

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

#Board
Tic = Tictactoe.Tictactoe()

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

def clear():
    for i in range(num_pixels):
        
        pixels[i] = (0,0,0)
    pixels.show()
             



# Comment this line out if you have RGBW/GRBW NeoPixels
pixels.fill((255, 0, 0))
# Uncomment this line if you have RGBW/GRBW NeoPixels
# pixels.fill((255, 0, 0, 0))
pixels.show()
time.sleep(1)

# Comment this line out if you have RGBW/GRBW NeoPixels
pixels.fill((0, 255, 0))
# Uncomment this line if you have RGBW/GRBW NeoPixels
# pixels.fill((0, 255, 0, 0))
pixels.show()
time.sleep(1)

# Comment this line out if you have RGBW/GRBW NeoPixels
pixels.fill((0, 0, 255))
# Uncomment this line if you have RGBW/GRBW NeoPixels
# pixels.fill((0, 0, 255, 0))
pixels.show()
time.sleep(1)

 
while True:
    clear()
    pixels.show()

    time.sleep(1)

    x = (input("enter n for new game , q to quit \n"))
    if(x == "n"):
        while True:
            b = input(" enter x to place x or o to place o, q to quit ")
            if(b == "x"):
                row = int(input("what row? "))
                col = int(input("what col? "))
                Tic.placePeice('x',row,col)
            elif(b == "o"):
                row = int(input("what row? "))
                col = int(input("what col? "))  
                Tic.placePeice('o',row,col)
            elif(b == "q"):
                print("you quit")
                break
            else:
                print("invalid input")

            Tic.printArr()
            showBoard(Tic)
            pixels.show()
            

            if(Tic.checkWin("x")):
                print(" x won! good job")
                break
            if(Tic.checkWin("o")):
                print(" o won! good job")
                break
    
    elif(x == "q"):
        break

    else:
        print("invalid input")
                      
        

    

clear()
pixels.show()
time.sleep(1)   
      


