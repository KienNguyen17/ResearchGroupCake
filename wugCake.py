import tkinter as tk
from PIL import Image, ImageTk
import random

#Hi Kien, Here is Runchen

class BasicGui: 

    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Happy Birthday!")

        self.mainCanvas = tk.Canvas(self.rootWin)
        self.mainCanvas.config(
            width=400,
            height=300,
            bd=2,
            relief=tk.RAISED,
            bg="#f3eed5"
        )
        # mainCanvas.pack()
        self.mainCanvas.grid(row=0, column=0, columnspan=4)

        self.submitButton = tk.Button(self.rootWin,
            text="Set Wug Number",
            font = "Times 12",
            fg = "blue",
            justify = tk.CENTER,
            bd = 10,
            command= lambda : self.addWug(int(self.wugEntry.get())) 
        )
        
        self.submitButton.grid(row = 1, column = 2)

        self.wugEntry = tk.Entry(self.rootWin)
        self.wugEntry.config(
            font = "Times 12",
            justify = tk.CENTER,
            fg = "black",
            bg = "white"
        )
        self.wugEntry.grid(row = 1, column = 1)

        self.photo = Image.open("./img/wug.png").resize((90, 110))
        self.wugList = []

    def addWug(self, num):
        self.wugList = []
        for i in range(num):
            self.wugList.append(ImageTk.PhotoImage(self.photo))

        for (j, wug) in enumerate(self.wugList):
            self.mainCanvas.create_image(random.randrange(0,400), random.randrange(0,300), image=wug)

    def run(self):
        self.rootWin.mainloop()

myGui = BasicGui()
myGui.run()
