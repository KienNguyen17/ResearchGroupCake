import tkinter as tk
from PIL import Image, ImageTk
import random
from wugFunction import *

#Hi Kien, Here is Runchen

class BasicGui: 

    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Happy Birthday!")
        self.HEIGHT = 600
        self.WIDTH = 800

        self.mainCanvas = tk.Canvas(self.rootWin)
        self.mainCanvas.config(
            width=self.WIDTH,
            height=self.HEIGHT,
            bd=2,
            relief=tk.RAISED,
            bg="#f3eed5"
        )
        self.mainCanvas.grid(row=0, column=0, columnspan=4)

        # Button will fetch wugEntry's input, convert to int and feed to addWud function
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

        # Convert to Image object
        # self.photo = Image.open("./img/wug.png").resize((90, 110))
        self.cakePic = Image.open("./img/cake.png").resize((250, 250))
        self.cakeCommand = ImageTk.PhotoImage(self.cakePic)

        # # List to contain ImageTk object, or else it gets deleted by garbage collector
        # self.wugList = []

        # Click this button to show a birthday cake and "happy birthday"
        self.surpriseButton = tk.Button(self.rootWin,
            text="🌟Surprise!🌼",
            font = "Times 12",
            fg = "blue",
            justify = tk.CENTER,
            bd = 10,
            command = self.birthdayText)
        self.surpriseButton.grid(row=2, column=2)

    def birthdayText(self):
        self.mainCanvas.create_text(400, 150, text="🎂HAPPY BIRTHDAY, Suhas!!!🍰",
                                  fill="darkblue", font = ("Comic Sans MS", 35))
        self.mainCanvas.create_text(200, 450, text="🎂",
                                  fill="blue", font = "Arial 300")
        #self.mainCanvas.create_text(650, 350, text="🧋",
                                    #fill="blue", font="Arial 300")
        self.mainCanvas.create_image(650, 350, image=self.cakeCommand)
        self.mainCanvas.create_text(600, 550, text="From your lovely research students✨",
                                    fill="darkblue", font=("Comic Sans MS", 15))



    def addWug(self, num):
        self.mainCanvas.delete(tk.ALL)
        # Reset the list
        # self.wugList = []
        for i in range(num):
        #     self.wugList.append(ImageTk.PhotoImage(self.photo))

        # # Randomly generate the coordinates for new wug images
        # for (j, wug) in enumerate(self.wugList):
            # self.mainCanvas.create_image(random.randrange(0,400), random.randrange(0,300), image=wug)
            self.addOneWug(random.randrange(0,self.WIDTH), random.randrange(0,self.HEIGHT))
            
    def addOneWug(self, x, y):
        x1, y1 = 10, 0
        x2, y2 = 40, 0
        x3, y3 = 0, 25
        x4, y4 = 60, 17
        points1 = bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4, tk=True)

        # Second curve control points
        a1, b1 = 10, 0
        a2, b2 = 80, -5
        a3, b3 = 38, 17
        a4, b4 = 60, 17
        points2 = bezier_curve(a1, b1, a2, b2, a3, b3, a4, b4, tk=True)

        #leg left
        i1, j1 = 33, 1
        i2, j2 = 32, -3
        i3, j3 = 30, -4
        i4, j4 = 29, -4.5
        points3 = bezier_curve(i1, j1, i2, j2, i3, j3, i4, j4, tk=True)

        #leg right
        h1, k1 = 45, 0.5
        h2, k2 = 46, -1
        h3, k3 = 47, -3.5
        h4, k4 = 45, -4.5
        points4 = bezier_curve(h1, k1, h2, k2, h3, k3, h4, k4, tk=True)

        #leg foot
        q1, p1 = 26.5, -4.5
        q2, p2 = 29, -4.6
        q3, p3 = 33, -4
        q4, p4 = 35, -4.5
        points5 = bezier_curve(q1, p1, q2, p2, q3, p3, q4, p4, tk=True)

        #right foot
        w1, z1 = 45, -4.5
        w2, z2 = 48, -4.5
        w3, z3 = 52, -4.3
        w4, z4 = 53, -4.5
        points6 = bezier_curve(w1, z1, w2, z2, w3, z3, w4, z4, tk=True)

        self.mainCanvas.create_polygon(*(points1 + points2), fill = "lightblue", smooth = True, width = 3, tags=("wug" + str(x) + str(y)))
        self.mainCanvas.create_line(*(points3), fill = "blue", smooth = True, width = 3, tags=("wug" + str(x) + str(y)))
        self.mainCanvas.create_line(*(points4), fill = "blue", smooth = True, width = 3, tags=("wug" + str(x) + str(y)))
        self.mainCanvas.create_line(*(points5), fill = "blue", smooth = True, width = 3, tags=("wug" + str(x) + str(y)))
        self.mainCanvas.create_line(*(points6), fill = "blue", smooth = True, width = 3, tags=("wug" + str(x) + str(y)))

        self.mainCanvas.create_oval(-50, -18, -44, -10, fill="black", tags=("wug" + str(x) + str(y)))
        for i in self.mainCanvas.find_withtag("wug" + str(x) + str(y)):
            self.mainCanvas.move(i, x, y)

    def run(self):
        self.rootWin.mainloop()

myGui = BasicGui()
myGui.run()
