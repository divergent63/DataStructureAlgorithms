
class BinaryTree():
    def __init__(self, RootVal):
        self.RootVal = RootVal
        self.LeftChild = None
        self.RightChild = None
        pass

    def InsertLeft(self, val):
        t = BinaryTree(val)
        if self.LeftChild is None:
            self.LeftChild = t
        else:
            t.LeftChild = self.LeftChild
            self.LeftChild = t
        return self

    def InsertRight(self, val):
        t = BinaryTree(val)
        if self.RightChild is None:
            self.RightChild = t
        else:
            t.RightChild = self.RightChild
            self.RightChild = t
        return self

    def GetLeftChild(self):
        return self.LeftChild

    def GetRightChild(self):
        return self.RightChild

    def GetRootVal(self):
        return self.RootVal

    def SetRootVal(self, NewVal):
        self.RootVal = NewVal


if __name__ == '__main__':
    bt = BinaryTree(1).InsertLeft(3).InsertLeft(2).InsertRight(1.5)
    print(bt.GetLeftChild().GetRootVal())
    print()
