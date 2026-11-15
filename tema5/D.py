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

    def max_2(self):
        node = self.root
        prev = None
        while node.right is not None:
            prev = node
            node = node.right
        if node.left is not None:
            otv = node.left
            while otv.right is not None:
                otv = otv.right
            return otv.data
        else:
            return prev.data

tree = BinarySearchTree()

for s in input().split():
    i = int(s)
    if i == 0:
        break
    tree.insert(i)
print(tree.max_2())

