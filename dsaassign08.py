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
ob = Graph(3)
ob.addEdge()
ob.display()

