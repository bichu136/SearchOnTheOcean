import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from PIL import Image , ImageTk
obstacles = []
fuelIsl = []
def drawGrid(Canvas):
    for i in range(25):
        Canvas.create_line(i*20 , 0 , i * 20 , 500)
    for i in range(25):
        Canvas.create_line(0 , i * 20, 500, i * 20 )
def drawBoat(Canvas,x,y):
    img = Image.open("boat.png")
    img = img.resize((18,18),Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    #Canvas.grid()
    h = imgtk.height()
    w = imgtk.width()
    global boatimg
    boatimg = imgtk
    Canvas.create_image(x,y,image = boatimg,anchor = "nw")
def drawObstacle(Canvas,x,y):
    img = Image.open("obstacle.png")
    img = img.resize((18, 18), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    # Canvas.grid()
    global obstacles
    obstacles.append(imgtk)
    Canvas.create_image(x, y, image=imgtk, anchor="nw")
def drawFuel(Canvas,x,y):
    img = Image.open("fuel.png")
    img = img.resize((18, 18), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    # Canvas.grid()
    global fuelIsl
    obstacles.append(imgtk)
    Canvas.create_image(x, y, image=imgtk, anchor="nw")

def drawGoal(Canvas, x, y):
    img = Image.open("goal.png")
    img = img.resize((40,20), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    # Canvas.grid()
    global goal
    goal= imgtk
    Canvas.create_image(x-7, y-3, image=goal, anchor="nw")