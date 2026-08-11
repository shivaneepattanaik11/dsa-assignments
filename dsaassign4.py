#create binary tree and perform inorder, preorder and postorder recursive traversal
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

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)  #recursive function
        preorder(root.right) #recursive function

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)  
        inorder(root.right) 


root=create()
print("preorder traversal is:\n")
preorder(root)
print("inorder traversal is:\n")
inorder(root)