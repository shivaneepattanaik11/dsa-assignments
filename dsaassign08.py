class Graph:
    def __init__(self,v):
        self.vertices=v
        self.AdjL=[[] for i in range (v) ]

    def addEdge(self):
        e=int(input("enter no. of edges:"))
        for i in range(e):
            print(f"enter edge {i+1}:")
            u=int(input("enter starting vertex:"))
            v=int(input("enter ending vertex:"))
            self.AdjL[u].append(v) #for undirected graph
            self.AdjL[v].append(u) #for undirected graph 

    def display(self):
        for i in range(self.vertices):
            print(i,"->",self.AdjL[i]) 
    
    def bfs(self,start):
        visited=[False]*self.vertices
        q=Queue()
        q.insert(start)
        visited[start]=True 
        while q.F!=-1:
            current=q.delete()
            print(current)

            for vertex in self.AdjL[current]:
                if visited[vertex]==False:
                    visited[vertex]=True
                    q.insert(vertex)


class Queue :
    def __init__(self):
        self.F=-1
        self.R=-1
        self.QT=[0]*5 #Queue size is fixed to 5 , not more than 5 elements are possible
    

    def insert(self,x):
        if self.R==4:
            print("Queue is overflow....")
            return
        self.R=self.R+1

        self.QT[self.R]=x

        if self.F==-1:
            self.F=0

    def delete(self):
        if self.F==-1:
            print("Nothing to  print..")
            return
        else:
            y=self.QT[self.F]

        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1
        return y

ob = Graph(3)   
ob.addEdge()
ob.display()
start=int(input("enter start vertex:"))
ob.bfs(start)

