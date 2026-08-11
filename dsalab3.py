#queue using class 
class queue:
    def __init__(self):
        self.F=-1
        self.R=-1
        self.qt=[0]*5
    def insert(self,x):
        if self.R==4:
            print("queue is full")
            return
        self.R+=1
        self.qt[self.R]=x
        if self.F==-1:
            self.F=0
    def delete(self):
        if self.F==-1:
            print("queue is empty")
            return
        else:
            y=self.qt[self.F]

        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F+=1
        return y
    def display(self):
        if self.F==-1:
            print("empty")
            return
        for i in range(self.F,self.R+1):
            print(self.qt[i])
q=queue()

while True:
    print("what you want to do?:")
    print("1. add.\n2. delete.\n3. display.")
    ch=int(input("enter choices:"))
    if ch==1:
        x=int(input("enter x:"))
        q.insert(x)
    elif ch==2:
        q.delete()
    elif ch==3:
        q.display()
        
    else:
        break
