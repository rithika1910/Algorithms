from collections import defaultdict
import numpy as np 
import time
import matplotlib.pyplot as plt
runtime = []
x = ["Kruskal's algorithm","Prim's algorithm","Boruvka's algorithm"]
class Heap():
    def __init__(self):
        self.heapList= [[-1,-np.inf]]
        self.currentSize = 0
        self.vertices = [-1]
        
    def Node(self, v, w):
        minHeapNode = [v, w]
        return minHeapNode

    def upHeapp(self,i):
        while(i>0):
            if(self.heapList[i//2][1]>self.heapList[i][1]):
                t=self.heapList[i]
                self.heapList[i]=self.heapList[i//2]
                self.heapList[i//2]=t
            i-=1
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.upHeapp(self.currentSize)
		
    def downHeap(self,i):
        while((i*2)<self.currentSize):
            m=self.minChild(i)
            if(self.heapList[m][1]<self.heapList[i][1]):
                t=self.heapList[m]
                self.heapList[m]=self.heapList[i]
                self.heapList[i]=t
            i=m	

    def minChild(self,i):
        if (((i*2)+1)>self.currentSize-1 or self.heapList[(i*2)+1][1]>self.heapList[(i*2)][1]):
            return (i*2)
        else:
            return (i*2)+1 

    def delMin(self):
        node_removed = self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize-=1
        self.downHeap(1)
        return node_removed
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):  
            self.downHeap(i)
            i = i - 1
            
    def update_weight(self, v, w):
        # Get the index of v in heap array
        self.vertices = [row[0] for row in self.heapList]
        index=self.vertices.index(v)
        # Get the node and update its weight
        self.heapList[index][1] = w
        self.upHeapp(index)
        
    def isInMinHeap(self, v):
        self.vertices = [row[0] for row in self.heapList]
        return (v in self.vertices)
    
    def isEmpty(self):
        return (self.currentSize == 0)

    def printHeap(self):
        print (self.heapList)
        
class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.edge_graph = []
        self.adj_graph = defaultdict(list)
    
    #edge list    
    def addin_edge(self, u, v, w):
        self.edge_graph.append([u, v, w])
        
    #adjacency map
    def addin_adj(self, u, v, w):
        newNode = [v, w]
        self.adj_graph[u].append(newNode)
        newNode = [u, w]
        self.adj_graph[v].append(newNode)
    
    #to return the absolute parent of i 
    def find_component(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_component(parent, parent[i])

    #to merge the two into a single component with common root(absolute parent)
    def merge_component(self, parent, x, y):
        parent[y]=x

    def kruskal_mst(self):
        MSTweight = 0
        mst = []
        i, e = 0, 0
        #sort the edge list based on the weight (key- edge[2])
        self.edge_graph = sorted(self.edge_graph, key= lambda edge: edge[2])
        parent = []
        for node in range(self.V):
            parent.append(node)

        while e < self.V - 1:
            u, v, w = self.edge_graph[i]
            i = i + 1
            x = self.find_component(parent, u)
            y = self.find_component(parent, v)
            #to check whether u,v belong to different component 
            #using their absolute parent
            if x != y:
                e = e + 1
                mst.append([u, v, w])
                MSTweight+=w
                self.merge_component(parent, x, y)
        
        print("*** MST through KRUSKAL algorithm ***")       
        for u, v, weight in mst:
            print("% d - % d : %d" % (u, v, weight))
        print ("Weight of MST is ", MSTweight) 
        print()
            
    def prims_mst(self):
        parent,weight = [-1],[0]
        pq = Heap()
 
        # Initializing heap with vertices and weight infinity
        for v in range(0,self.V):
            parent.append(-1)
            weight.append(np.inf)
            pq.insert(pq.Node(v,weight[v+1]))
            pq.vertices.append(v)
            
        # weight of 0th vertex = 0 and updating in heap
        weight[1] = 0
        pq.update_weight(0, weight[1])
 
        # heap has all nodes not yet added in the MST.
        while (not pq.isEmpty()):
            # Extract the vertex with minimum weight
            newHeapNode = pq.delMin()
            u = newHeapNode[0]
 
            # Traverse through all adjacent vertices of u (the extracted vertex) and update their weight
            for neigbhour in self.adj_graph[u]:
                v = neigbhour[0]
                # if adjnode is in heap(not part of mst) and its weight in heap is large than extracted adjnode's weight
                if pq.isInMinHeap(v) and neigbhour[1] < weight[v+1]:
                    weight[v+1] = neigbhour[1]
                    parent[v+1] = u
                    # update weight in min heap also
                    pq.update_weight(v, weight[v+1])
        
        print("*** MST through PRIM'S algorithm ***")
        MSTweight=0
        for i in range(2, self.V+1):
            MSTweight+=weight[i]
            print("% d - % d : %d" % (parent[i], i-1, weight[i]))
        print ("Weight of MST is ", MSTweight)
        print()
    
    def boruvka(self):
        mst=[] 
        parent = []
        cheapest =[]      
        numTrees = self.V 
        MSTweight = 0     
        for node in range(self.V): 
            parent.append(node)  
            cheapest =[-1] * self.V 
        while numTrees > 1: 
            for i in range(len(self.edge_graph)): 
                u,v,w = self.edge_graph[i] 
                set1 = self.find_component(parent, u) 
                set2 = self.find_component(parent ,v) 

               
                if set1 != set2:   
                    if cheapest[set1] == -1 or cheapest[set1][2] > w : 
                        cheapest[set1] = [u,v,w] 
                    if cheapest[set2] == -1 or cheapest[set2][2] > w : 
                        cheapest[set2] = [u,v,w] 

            for node in range(self.V): 
                if cheapest[node] != -1: 
                    u,v,w = cheapest[node] 
                    set1 = self.find_component(parent, u) 
                    set2 = self.find_component(parent ,v) 

                    if set1 != set2 : 
                        MSTweight += w 
                        self.merge_component(parent, set1, set2) 
                        mst.append([u, v, w])
                        numTrees = numTrees - 1
            cheapest =[-1] * self.V 

        
        print("*** MST through BORUVKA'S algorithm ***")       
        for u, v, weight in mst:
            print("% d - % d : %d" % (u, v, weight))
        print ("Weight of MST is %d" % MSTweight) 
        print()

f = open("mst_input.txt","r")
for line in f:
    runtime = []
    l = line.split(" ")
    g = Graph(int(l[0]))
    print(l)
    print()
    for i in range(1,len(l)):
        u,v,w=map(int,l[i].split(","))
        g.addin_edge(u,v,w)
        g.addin_adj(u,v,w)
    
    start = time.time()
    g.boruvka()
    end = time.time()
    runtime.append(end - start)
    
    start = time.time()
    g.prims_mst()
    end = time.time()
    runtime.append(end - start)
    start = time.time()
    
    g.kruskal_mst()
    end = time.time()
    runtime.append(end - start)
    plt.plot(x,runtime,"--o")
    plt.legend(['G1-6V,8E','G2-6V,15E','G3-6V,8E','G4-8V,12E','G5-8V,11E','G6-18V,33E'],bbox_to_anchor = (1.05, 0.6))
    plt.xlabel('Algorithms')
    plt.ylabel('Execution time')
plt.show()
f.close()

