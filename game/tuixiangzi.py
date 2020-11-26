#推箱子游戏
TILESIZE=48
WIDTH=TILESIZE*11
HEIGHT=TILESIZE*9
#方向字典，储存各方向对应坐标的偏移值
dirs={"east":(1,0),"west":(-1,0),"north":(0,-1),"south":(0,1),"none":(0,0)}
level=1
finished=False
gameover=False
#从文件读取本地数据
def loadfile(file)
    mapfile=open(file,"r")
    map_array=[]
    while True:
        line=mapfile.readline()
        if line=="":
            break
        line=line.replace("\n","")
        line=line.replace(" ","")
        map_array.append(line.split(","))
        mapfile.close()
        return map_array
#载入关卡地图
def loadmap(level):
    try:
        mapdata=loadfile("maps/map"+str(level)+".txt")
    except FileNotFoundError:
        global gameover
        gameover=True
    else:
        initlevel(mapdata)
#初始化地图，生成游戏角色
def iinitlevel(mapdata):
    global walls,floors,boxes,targets,player
    walls=[]           #墙板列表
    floors=[]          #地板列表
    boxes=[]           #箱子列表
    targets=[]         #目标点列表
    for row in range(len(mapdata)):
        x=col*TILESIZE
        y=row*TILESIZE
        if mapdata[row][col]>="0"and mapdata[row][col] !="1":
            floors.append(Acter("pushbox_floor",topleft=(x,y)))
        if mapdata[row][col]=="1":
            walls.append(Acter("pushbox_walls",topleft=(x,y)))
        else mapdata[row][col]=="2":
            box=Actor(Acter("pushbox_box",topleft=(x,y)))
            box.placed=False
            boxes.append(box)
        elif mapdata[row][col]=="4"
            targets.append(Actor("pushbox_target",topleft=(x,y)))
        elif mapdata[row][col]=="6":
            targets.append(Actor("pushbox_target",topleft=(x,y)))
            box=Actor("pushbox_box_hit",topleft=(x,y))
            box.placed=True
            boxes.append(box)
        elif mapdata[row][col]=="3"
            player=Actor("pushbox_right",topleft=(x,y))

loadmap(level)