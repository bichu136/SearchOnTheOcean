import OnTheOceanObject as MyObj
#--------GLOBAL VARIABLE----------#
boat = None
goal = None
open = None
close = []
path = []
fuel_a = None
def get_path(Boat,map):
    global path
    if map.grids[Boat.y][Boat.x].fr is not None:
        path.append(Boat)
        get_path(map.grids[Boat.y][Boat.x].fr,map)
#Thuật giải gốc
def get_true_fuel(map):
    global boat,goal
    islands = []
    islands.append({"pos": boat, "vertexes": [],"visitted" :False,"p":None})
    for y in range(25):
        for x in range(25):
            if map.grids[y][x].type ==2:
                islands.append({"pos":MyObj.pos(x,y),"vertexes":[],"visitted" :False,"p":None})
    islands.append({"pos":goal,"vertexes":[],"visitted" :False,"p":None})
    for island in islands:
        for other in islands:
            if island is other:
                continue
            if island["pos"].distance(other["pos"])<=fuel_a:
                island["vertexes"].append(other)
    t_open = []
    t_open.append(islands[0])
    path = []
    while t_open!=[]:
        c = t_open[0]
        if c["visitted"]:
            t_open.remove(c)
            continue
        c["visitted"]= True
        if c["pos"]==goal:
            p = c
            while(p is not None):
                path.append(p["pos"])
                p=p["p"]
            break
        for pos in c["vertexes"]:
            if pos["visitted"]:
                continue
            pos["p"] = c
            t_open.append(pos)
        t_open.remove(c)
    if path == []:
        return
    for island in islands:
        if island["pos"] not in path:
            map.grids[island["pos"].y][island["pos"].x].type = 1

def bfs_recursive(map):
    global boat,goal,open,close
    if open is None:
        map.grids[boat.y][boat.x].current_fuel = fuel_a
        get_true_fuel(map)

        open = [boat]
    else:
        if open ==[]:
            return
        C = open[0]
        if map.grids[C.y][C.x].unvisited == False:
            open.remove(C)
            return
        map.grids[C.y][C.x].unvisited = False
        if C== goal:
            print("have get to the goal")
            get_path(C,map)
            # for x in path:
            #     print(x)
        cg = C.can_go(map)
        for position in cg:
            if map.grids[position.y][position.x].current_fuel < map.grids[C.y][C.x].current_fuel:
                map.grids[position.y][position.x].current_fuel = map.grids[C.y][C.x].current_fuel
                map.grids[position.y][position.x].fr = C
            map.grids[position.y][position.x].current_fuel -=1
            if map.grids[position.y][position.x].type == 2:
                map.grids[position.y][position.x].current_fuel +=fuel_a
            if map.grids[position.y][position.x].current_fuel >=0:
                open.append(position)
        close.append(C)
        open.remove(C)
