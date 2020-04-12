class Grid():
    def __init__(self):
        self.fr = None
        self.type = 0
        self.unvisited = True
        self.current_fuel = -1
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
    def __init__(self,x,y):
        self.x = x
        self.y= y
    def can_go(self,grid):
        cg = []

        tu = pos(self.x,self.y-1)
        if tu.check_collision(grid):
            cg.append(tu)
        td = pos(self.x,self.y+1)
        if td.check_collision(grid):
            cg.append(td)
        tl = pos(self.x-1,self.y)
        if tl.check_collision(grid):
            cg.append(tl)
        tr = pos(self.x+1,self.y)
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
        if grid.grids[self.y][self.x].type==1:
            return False
        if grid.grids[self.y][self.x].unvisited:
            return True
        else:
            return False
    def distance(self,other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
