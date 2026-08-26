class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


def insert(root, book):
    if root is None:
        return Node(book)

    if book < root.book:
        root.left = insert(root.left, book)
    else:
        root.right = insert(root.right, book)

    return root


# Inorder: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.book, end=" ")
        inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.book, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.book, end=" ")


# Main
root = None

root = insert(root, "DSA")
insert(root, "DBMS")
insert(root, "C++")
insert(root, "Python")
insert(root, "Java")

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)