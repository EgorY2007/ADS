class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key == node.data:
                return
            elif key < node.data:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right

    def razvil(self, node):
        if node is None:
            return
        if node.left is not None:
            self.razvil(node.left)
        if node.left is not None and node.right is not None:
            print(node.data)
        if node.right is not None:
            self.razvil(node.right)
            
tree = BinarySearchTree()

for s in input().split():
    i = int(s)
    if i == 0:
        break
    tree.insert(i)
tree.razvil(tree.root)
