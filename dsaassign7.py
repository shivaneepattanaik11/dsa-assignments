class graph:
    def __init__(self):
        self.v=0 #vertice
        self.e=0 #edges
        self.g=[[0 for i in range(9)] for j in range(9)]
    def create(self):
        self.v=int(input("enter number of vertices:"))
        self.e=int(input("enter numbe rof edges:"))

        for i in range(self.e):
            print(f"enter egde {i+1}:")
            u=int(input("enter starting vertex:"))
            v=int(input("enter ending vertex:"))
            w=int(input("enter weight:"))  #optional, this makes the graph weighted!!
            self.g[u][v]=self.g[v][u]=w 
            #for undirected graph for directed graph self.g[u][v]=1 (directed non-weighted graph)
    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.g[i][j],end=" ")
            print()
class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x
    
def dfs(ob,start):
    visited=[False]*ob.v
    s=Stack()
    s.push(start)
    while s.TOP!=-1:
        u=s.pop()
        if visited[u]==False:
            print(u,end=" ")
            visited[u]=True
        for v in range(ob.v-1,-1,-1):
            if (ob.g[u][v]!=0 and visited[v]==False):  #it will tell whether edge exists or not
                s.push(v)
ob=graph()
ob.create()
ob.display()
start=int(input("enter start vertex:"))
print("dfs:",dfs(ob,start))

