class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def LNR(self, root):
        kq = []
        if root:
            kq = self.LNR(root.left)
            kq.append(root.data)
            kq = kq + self.LNR(root.right)
        return kq
# Left-Right-Root
    def LRN(self, root):
        kq = []
        if root:
            kq = self.LRN(root.left)
            kq = kq + self.LRN(root.right)
            kq.append(root.data)
        return kq
# Root -> Left ->Right
    def NLR(self, root):
        kq = []
        if root:
            kq.append(root.data)
            kq = kq + self.NLR(root.left)
            kq = kq + self.NLR(root.right)
        return kq
# Root-Right-Left
    def NRL(self, root):
        kq = []
        if root:
            kq.append(root.data)
            kq = kq + self.NLR(root.right)            
            kq = kq + self.NLR(root.left)
        return kq
# Right-Root-Left
    def RNL(self, root):
        kq =[]
        if root:
            kq = self.RNL(root.right)
            kq.append(root.data)
            kq = kq + self.RNL(root.left)
        return kq
# Right-Left-Root
    def RLN(self, root):
        kq = []
        if root:
            kq =  self.RLN(root.right)
            kq = kq + self.RLN(root.left)
            kq.append(root.data)
        return kq
#[42, 31, 35, 19, 10, 14, 27]
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("-----LNR-------")
print(root.LNR(root))
print("-----LRN-------")
print(root.LRN(root))
print("-----NLR-------")
print(root.NLR(root))
print("-----NRL-------")
print(root.NRL(root))
print("-----RNL-------")
print(root.RNL(root))
print("-----RLN-------")
print(root.RLN(root))
