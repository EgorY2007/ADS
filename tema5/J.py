class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
        
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
                node.count += 1
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

    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print(node.data, node.count)
        self.print_tree(node.right)
        
tree = BinarySearchTree()

for s in input().split():
    i = int(s)
    if i == 0:
        break
    tree.insert(i)
tree.print_tree(tree.root)
