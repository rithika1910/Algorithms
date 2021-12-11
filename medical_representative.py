import math

def modified_floydWarshall(dist, V):
    for k in range(0,V):
        for i in range(0,V):
            for j in range(0,V):
                if (dist[i][k] == -math.inf or dist[k][j] == -math.inf):
                    continue
                if (dist[i][j] < dist[i][k]+dist[k][j]):
                    dist[i][j] = dist[i][k]+dist[k][j]
                    nextcity[i][j] = nextcity[i][k]
    return dist, nextcity
                
def findPath(u, v):
    if (nextcity[u][v] == -1):
        return []
    path = [u]
    while (u != v):
        u = nextcity[u][v]
        path.append(u)
    return path

def printPath(path):
    lp = len(path)
    for i in range(0,lp-1):
        print(path[i]+1, end = ',')
    print(path[lp - 1] +1)

n = int(input())
k = int(input())
priority = input().split(' ')
priority = [int(j) for j in priority]
adjmat =[]
rows, cols = (n, n)
dist = [[0 for i in range(cols)] for j in range(rows)]
nextcity = [[0 for i in range(cols)] for j in range(rows)]

for i in range(0,n):
    l = []
    for j in range(0,n):
        if (priority[i] == priority[j]-1):
            l.append(abs(j-i))
        else:
            l.append(-math.inf)
    adjmat.append(l)

for i in range(0, n):
    for j in range(0,n):
        dist[i][j] = adjmat[i][j]
        if (adjmat[i][j] == -math.inf):
            nextcity[i][j] = -1
        else:
            nextcity[i][j] = j
            
dist, nextcity = modified_floydWarshall(dist,n)
maxx = -math.inf
for i in range(0,n):
    for j in range(0,n):
        if(priority[j]==k and dist[i][j]!=-math.inf and maxx<dist[i][j]):
            maxx=dist[i][j]
            fromm=i
            to=j
if (maxx == -math.inf):
    print('0')
else:
    print(maxx)
    
if(maxx != -math.inf):
    path = findPath(fromm, to)
    printPath(path)

