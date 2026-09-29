#6a.create a binary search tree print the original and new tree level-wise find height and print leaf nodes

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None 
        self.data=data

def insert(root,x):
    if root==None:
        return Node(x)
    if root.data<x:
        root.right=insert(root.right,x)
    else:
        root.left=insert(root.left,x)
    return root

def create():
    root=None
    while True:
        x=int(input("enter data to create node(0 to stop):"))
        if x==0:
            break
        root=insert(root,x)
    return root

#recursive inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

#queue
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
    
    def display(self):
        if self.F==-1:
            print("Nothing to print")
            return
        for i in range(self.F,self.R+1):
            print(self.QT[i])

def level_wise(root):
    if root is None:
        return 
    q=Queue()
    q.insert(root)
    while q.F!=-1:
        r=q.delete()
        print(r.data)

        if r.left!= None:
            q.insert(r.left)
        if r.right != None:
            q.insert(r.right)

def height(root):
    if root== None:
        return 0
    left_height=height(root.left)
    right_height=height(root.right)

    return max(left_height,right_height)+1

def leaf_node(root): #left
    if root is None:
        return
    if root.left==None and root.right==None:
        print(root.data)
    
    leaf_node(root.left)
    leaf_node(root.right)


r=create()
inorder(r)
print("\nlevel wise traversal:")
level_wise(r) 
print("\nheight of the tree:",height(r))
print("\nleaf node:")
leaf_node(r)
