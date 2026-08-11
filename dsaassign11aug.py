class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create():
    n=int(input("enter data to create node (0 to stop):"))
    if n==0:        #0 is used to stop the formnation of tree in one direction. 
        return None 
    root=Node(n) #object creation
    print(f"enter left of {n}:")
    root.left=create()
    print(f"enter right of {n}:")
    root.right=create()
    return root

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

def preorder(root):
    s=Stack()
    while root is not None:
        print(root.data)
        s.push(root)
        root=root.left
    while s.top!=-1:
        temp=s.pop()
        temp=temp.right
    while root is not None:
        print(root.data)
        s.push(root)
        root=root.left

root=create()
print("preorder traversal is:\n")
preorder(root)
