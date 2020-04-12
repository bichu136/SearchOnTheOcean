import sys
import SearchingRecursive as SR
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
def addObstacles(x,y):
    img = Image.open("obstacle.png")
    img = img.resize((18, 18), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    # Canvas.grid()
    global obstacles
    obstacles.append({"img": imgtk, "X": x, "Y": y})
def drawObstacle(Canvas):
    for obs in obstacles:
        Canvas.create_image(obs["X"],obs["Y"], image=obs["img"], anchor="nw")
def addFuel(x,y):
    img = Image.open("fuel.png")
    img = img.resize((18, 18), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    # Canvas.grid()
    global fuelIsl
    fuelIsl.append({"img": imgtk, "X": x, "Y": y})
def drawFuel(Canvas):
    for obs in fuelIsl:
        Canvas.create_image(obs["X"],obs["Y"], image=obs["img"], anchor="nw")
def drawOpen(Canvas):
    for pos in SR.open:
        x = pos[0]
        y = pos[1]
        Canvas.create_rectangle((x*20),(y*20),(x+1)*20,(y+1)*20,fill="brown")
def drawGoal(Canvas, x, y):
    img = Image.open("goal.png")
    img = img.resize((40,20), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    # Canvas.grid()
    global goal
    goal= imgtk
    Canvas.create_image(x-7, y-3, image=goal, anchor="nw")
def drawOpen(Canvas,O):
    for pos in O:
        Canvas.create_rectangle(pos.x*20,pos.y*20,(pos.x+1)*20,(pos.y+1)*20,fill = "red")
def drawPath(Canvas,P):
    for pos in P:
        Canvas.create_rectangle(pos.x*20,pos.y*20,(pos.x+1)*20,(pos.y+1)*20,fill = "green")
def drawClose(Canvas,C):
    for pos in C:
        Canvas.create_rectangle(pos.x*20,pos.y*20,(pos.x+1)*20,(pos.y+1)*20,fill = "pink")
def drawCurrent(Canvas,pos):
    Canvas.create_rectangle(pos.x * 20, pos.y * 20, (pos.x + 1) * 20, (pos.y + 1) * 20, fill="yellow")