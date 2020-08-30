
import tkinter as tk  

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import Tictactoe

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)

        self.Button1 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button2 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button3 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button4 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button5 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button6 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button7 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button8 = tk.Button(self, text='Quit',
            command=self.haha(1))

        self.Button9 = tk.Button(self, text='Quit',
            command=self.haha(1))                    


        self.quitButton.grid(column = 0 ,row = 0 )
        self.Button1.grid(column = 1 ,row = 0 )   
        self.Button2.grid(column = 1 ,row = 1 )
        self.Button3.grid(column = 1 ,row = 2 )
        self.Button4.grid(column = 2 ,row = 0 )
        self.Button5.grid(column = 2 ,row = 1 )
        self.Button6.grid(column = 2 ,row = 2 )
        self.Button7.grid(column = 3 ,row = 0 )
        self.Button8.grid(column = 3 ,row = 1 )
        self.Button9.grid(column = 3 ,row = 2 )


    def haha(self,jeex):
        print(jeex)             

app = Application()                       
app.master.title('Sample application')    
app.mainloop() 