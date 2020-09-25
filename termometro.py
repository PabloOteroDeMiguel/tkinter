from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        self.geometry("150x150")
        self.configure(bg="#DED7B9")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)        
    
    def start(self):
        self.mainloop()
        
if __name__ == '__main__':
    app = mainApp()
    app.start()