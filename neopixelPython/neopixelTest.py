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
    i = 7
    for row in range(row):
            for col in range(col):
                if(Tac.board == 'x'):
                    pixels[i] = (100,0,0)
                if(Tac.board == 'o'):
                    pixels[i] = (0,100,0)
                else:
                    pixels[i] = (0,0,100)
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
    for j in range(255):
        for i in range(num_pixels):
            
            pixels[i] = (0,0,0)
             



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
   showBoard(Tic)
   time.sleep(1)
   time.sleep(1)
   time.sleep(1)
   rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step


