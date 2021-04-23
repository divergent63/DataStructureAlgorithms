
"""
二叉树
二叉堆 （ 满二叉树 --> 平衡二叉树 ）
二叉搜索树
AVL树
"""
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

    def preorder(self, tree):
        # 前序遍历：根节点、左子树、右子树
        if tree:
            print(tree.RootVal)
            self.preorder(tree.GetLeftChild())
            self.preorder(tree.GetRightChild())

    def midorder(self, tree):
        # 前序遍历：根节点、左子树、右子树
        if tree:
            self.preorder(tree.GetLeftChild())
            print(tree.RootVal)
            self.preorder(tree.GetRightChild())

    def postorder(self, tree):
        # 前序遍历：根节点、左子树、右子树
        if tree:
            self.preorder(tree.GetLeftChild())
            self.preorder(tree.GetRightChild())
            print(tree.RootVal)


class BinaryHeap():
    def __init__(self):
        self.heap_lst = [0]
        self.size = 0

    def insert(self, val):
        self.size += 1
        i = self.size
        self.heap_lst.append(val)

        while i // 2 > 0:
            if val < self.heap_lst[i//2]:
                self.heap_lst[i] = self.heap_lst[i // 2]
                self.heap_lst[i // 2] = val
            i = i // 2
        return None


if __name__ == '__main__':
    # bt = BinaryTree(1).InsertLeft(3).InsertLeft(2).InsertRight(1.5)
    # # print(bt.GetLeftChild().GetRootVal())
    # print(bt.preorder(bt))

    bh = BinaryHeap()
    [bh.insert(i) for i in range(1, 8)]
    bh.insert(0.5)
    bh.insert(4.5)


