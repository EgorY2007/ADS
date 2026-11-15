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

    def _check(self, node):
        if node is None:
            return 0
        h_left = self._check(node.left)
        if h_left == -1:
            return -1
        h_right = self._check(node.right)
        if h_right == -1:
            return -1
        if abs(h_left - h_right) > 1:
            return -1
        return 1 + max(h_left, h_right)

    def is_balanced(self):
        return self._check(self.root) != -1
    
tree = BinarySearchTree()

for s in input().split():
    i = int(s)
    if i == 0:
        break
    tree.insert(i)
if tree.is_balanced():
    print('YES')
else:
    print('NO')
