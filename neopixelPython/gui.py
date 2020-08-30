
import tkinter as tk       

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.practiceButton = tk.Button(self, text='Quit',
            command=self.haha)                
        self.quitButton.grid(column = 0 ,row = 0 )
        self.practiceButton.grid(column = 1 ,row = 1 )   

    def haha(self):
        print("yoink")             

app = Application()                       
app.master.title('Sample application')    
app.mainloop() 