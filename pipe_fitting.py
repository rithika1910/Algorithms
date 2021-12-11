import math
b = 0
p = 0
fromm = []
to = []
diameter = []
give_to = [0]*100
get_from = [0]*100
d = [0]*100
min_diameter = 0

def traversal(building):
    global min_diameter
    if (give_to[building]==0):
        return building  #last building with the tap
    if (d[building]<min_diameter):
        min_diameter = d[building] # assign minimum diameter 
    return traversal(give_to[building])

def Solution(pipe_connections):
    global min_diameter
    i = 1
    while (i<p+1):
        give_to[pipe_connections[i][0]] = pipe_connections[i][1]
        d[pipe_connections[i][0]] = pipe_connections[i][2]
        get_from[pipe_connections[i][1]] = pipe_connections[i][0]
        i=i+1
    
    for building in range(1, b+1):
        if (get_from[building] == 0 and give_to[building]):
            min_diameter = math.inf
            last_building = traversal(building)
            fromm.append(building)
            to.append(last_building)
            diameter.append(min_diameter)
            
    print(len(fromm))
    for j in range(len(fromm)):
        print(fromm[j], to[j], diameter[j])


b = int(input()) #no. of buiding
p = int(input()) #no. of pipe

pipe_connections = [[0]*3]*p
for i in range(0,p):
    string = input().split(',')
    pipe_connections[i] = [int(i) for i in string]
pipe_connections.insert(0,[0,0,0])
Solution(pipe_connections);