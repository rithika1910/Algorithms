class Graph:
    adj = []
    numVertices=0
    def __init__(self,v):
        self.adj = [[0 for i in range(v)] 
                        for j in range(v)]
        self.numVertices= v

    def addEdge(self,f,t):  #f is from node, t is to node
        self.adj[f][t] = 1
    """
    Write a method to generate an adjacency matrix representation of the graph
    """
    def createAdjMatrix(self):
        return self.adj
    def printGraph(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print (self.adj[i][j]," ",end="")
            print ( "")
    def checkCourseConflictMap(self):
        #@start-editable@
        
        #adjacency list
        self.adjlist = {i: [] for i in range(self.numVertices)}
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                if self.adj[i][j]== 1:
                    self.adjlist[i].append(j)
                    
        visited = [False] * (self.numVertices)
        s = [False] * (self.numVertices)
        for vertex in range(self.numVertices):
            if visited[vertex] == False:
                if self.detect_cycle(vertex,visited,s) == True:
                    return True
        return False
    
    def detect_cycle(self,v,visited,s):
        visited[v] = True
        s[v] = True
        for neighbour in self.adjlist[v]:
            if visited[neighbour] == False:
                if self.detect_cycle(neighbour, visited, s) == True:
                    return True
            elif s[neighbour] == True:
                return True
        s[v] = False
        return False
        
        #@end-editable@
    
    def printMinimumSemesterDetails(self):
        #@start-editable@
        
        course_added = []
        semester = 0
        course_remaining = [i for i in range(self.numVertices)]
        while (len(course_remaining)) != 0:
            print(semester+1, end=" :")
            for i in course_remaining:
                f = 0
                for j in range(self.numVertices):
                    if self.adj[j][i] == 1:
                        f = 1
                        break
                if f == 0:
                    course_added.append(i)
                    print(i, end=",")
            for i in course_added:
                self.adj[i] = [0 for x in range(self.numVertices)]
                course_remaining.remove(i)
            course_added.clear()
            print("")
            semester += 1
        print(semester)
        
        #@end-editable@

def createCourseDependencyGraph():
    numvertex=int(input())
    g=Graph(numvertex)
    for i in range(numvertex):
        edgestr=str(input())
        edges = edgestr.split()
        node=int(edges[0])
        if ( len(edges) > 1):
            for j in (1,len(edges)-1):
                g.addEdge(int(edges[j]),node)
    return g

def indegree(mat,i):
    #@start-editable@

    pass
    
    #@end-editable@
def main():
    
    g = createCourseDependencyGraph()
    g.printGraph()
    if(g.checkCourseConflictMap() == False):
        g.printMinimumSemesterDetails()
    else:
        print("Conflict in pre-requisite mapping")
    
if __name__ == '__main__':
    main()
