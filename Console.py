import sys
import os

#-------class for easy read code------#
class Grid():
    def __init__(self):
        self.fr = None
        self.type = 0
        self.unvisited = True
class Map():
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.grids = []
        for i in range(height):
            self.grids.append([])
            for j in range(width):
                self.grids[i].append(Grid())
class pos():
    pass
    def __init__(self):
        pass
    def can_go(self,grid):
        cg = []
        tu = pos();tu.y = self.y -1;tu.x = self.x
        if tu.check_collision(grid):
            cg.append(tu)
        td = pos();td.y = self.y +1; td.x = self.x
        if td.check_collision(grid):
            cg.append(td)
        tl = pos();tl.x = self.x - 1;tl.y = self.y
        if tl.check_collision(grid):
            cg.append(tl)
        tr = pos();tr.x= self.x + 1;tr.y = self.y;
        if tr.check_collision(grid):
            cg.append(tr)
        return cg
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)
    def check_collision(self,grid):
        if self.x<0 or self.x >=grid.width:
            return False
        if self.y<0 or self.y>=grid.height:
            return False
        if grid.grids[self.y][self.x].type!=0:
            return False
        if grid.grids[self.y][self.x].unvisited:
            return True
        else:
            return False
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

#-----GLOBAL VARIABLE-----#
# 0 is available to go
# 1 is boat
# 9 is goal
Boat = pos()
Goal = pos()
map = Map(10,10)
open = []
close = []
path = []
def printMap():
    global map,Boat,Goal
    for i in range (map.height):
        for j in range(map.width):
            if Boat.x == j and Boat.y ==i:
                print("C",end=" ")
            elif Goal.x == j and Goal.y == i:
                print("G",end = " ")
            else:
                print(map.grids[i][j].type,end = " ")
        print()
def getBoat():
    global Boat
    print("give a position of boat")
    b = [int(x) for x in input().split(' ')]
    Boat.x = b[0]
    Boat.y = b[1]
def getGoal():
    global Goal
    print("give a position of goal")
    b = [int(x) for x in input().split(' ')]
    Goal.x = b[0]
    Goal.y = b[1]


def MenuConsole():
    print("--------------------------\nchoose the command:\n1.go to the next step\n0. exit")
    sel = int(input())
    return sel
os.system('clear')


def get_path(Boat):
    global path
    if map.grids[Boat.y][Boat.x].fr is not None:
        path.append(Boat)
        get_path(map.grids[Boat.y][Boat.x].fr)
def bfs_recursive():
    global map,Boat,Goal,open,close
    if open ==[]:
        open.append(Boat)
    else:
        C = open[0]
        if map.grids[C.y][C.x].unvisited == False:
            open.remove(Boat)
            return
        map.grids[C.y][C.x].unvisited = False
        if C== Goal:
            print("have get to the goal")
            get_path(C)
            for x in path:
                print(x)
            sys.exit()
        cg = Boat.can_go(map)
        for position in cg:
            map.grids[position.y][position.x].fr = Boat
            open.append(position)
        open.remove(C)