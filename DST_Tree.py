
"""
See also DST_NonLinearTable.py

二叉树
二叉堆 （ 平衡： 满二叉树 --> 完全二叉树 ）
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

    def Preorder(self, tree):
        # 前序遍历：根节点、左子树、右子树
        if tree:
            print(tree.RootVal)
            self.Preorder(tree.GetLeftChild())
            self.Preorder(tree.GetRightChild())

    def Midorder(self, tree):
        # 前序遍历：根节点、左子树、右子树
        if tree:
            self.Midorder(tree.GetLeftChild())
            print(tree.RootVal)
            self.Midorder(tree.GetRightChild())

    def Postorder(self, tree):
        # 前序遍历：根节点、左子树、右子树
        if tree:
            self.Postorder(tree.GetLeftChild())
            self.Postorder(tree.GetRightChild())
            print(tree.RootVal)


class BinaryHeap():
    """
    按序排列的完全二叉树，包括最大堆、最小堆，此处以最小堆实例化
    """
    def __init__(self):
        self.heap_lst = [0]
        self.size = 0

    def Insert(self, val):
        self.size += 1
        i = self.size
        self.heap_lst.append(val)

        while i // 2 > 0:
            if val < self.heap_lst[i//2]:
                self.heap_lst[i] = self.heap_lst[i // 2]
                self.heap_lst[i // 2] = val
            else:
                break
            i = i // 2
        return None

    def FindMin(self):
        if self.size > 0:
            return self.heap_lst[1]
        return None

    def FindMax(self):
        if self.size > 0:
            return max(self.heap_lst)
        return None

    def DelMin(self):
        """
        删除堆顶的最小节点，并将堆底节点填充到堆顶，然后重新调整堆顺序
        :return:
        """
        # 空树无最小
        if len(self.heap_lst) < 2:
            print('Empty heap has no minimize node')
            return

        self.heap_lst[1] = self.heap_lst[-1]
        self.heap_lst.pop()
        self.size -= 1

        i = 1
        while i * 2 < self.size:
            if i*2+1 > self.size:
                tmp = self.heap_lst[i*2]
                self.heap_lst[i*2] = self.heap_lst[i]
                self.heap_lst[i] = tmp
            elif self.heap_lst[i*2] > self.heap_lst[i*2+1]:
                tmp = self.heap_lst[i*2+1]
                self.heap_lst[i*2+1] = self.heap_lst[i]
                self.heap_lst[i] = tmp
            else:
                tmp = self.heap_lst[i*2]
                self.heap_lst[i*2] = self.heap_lst[i]
                self.heap_lst[i] = tmp
            i = i * 2
        return

    def IsEmpty(self):
        return True if len(self.heap_lst) > 1 else False

    def Size(self):
        return len(self.heap_lst) - 1

    def BuildHeap(self, lst):
        self.size = len(lst)
        self.heap_lst = [0] + lst
        # j = self.size
        # while j > 0:
        for j in range(self.size//2, 0, -1):
            i = j
            while i * 2 < self.size+1:
                if i * 2 + 1 > self.size:
                    tmp = self.heap_lst[i*2]
                    self.heap_lst[i*2] = self.heap_lst[i]
                    self.heap_lst[i] = tmp
                elif self.heap_lst[i*2] < self.heap_lst[i*2+1]:
                    tmp = self.heap_lst[i*2]
                    self.heap_lst[i*2] = self.heap_lst[i]
                    self.heap_lst[i] = tmp
                elif self.heap_lst[i*2] > self.heap_lst[i*2+1]:
                    tmp = self.heap_lst[i*2+1]
                    self.heap_lst[i*2+1] = self.heap_lst[i]
                    self.heap_lst[i] = tmp
                else:
                    break
                if j == 1:          # 需要再i=2重新赋值给j=1之前返回，负责进入死循环
                    return self.heap_lst
                i = i * 2


class TreeNode():
    def __init__(self, key, val, right, left, parent):
        self.key = key
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent


class BinarySearchTree():
    def __init__(self):

        pass


if __name__ == '__main__':
    # bt = BinaryTree(1).InsertLeft(3).InsertLeft(2).InsertRight(1.5)
    # # print(bt.GetLeftChild().GetRootVal())
    # print(bt.preorder(bt))

    """
             0.5
           /     \
         1         3
       /  \      /   \
      2    5    6     7
     / \ 
    4  4.5
    """
    bh = BinaryHeap()
    bh.DelMin()
    [bh.Insert(i) for i in range(1, 8)]
    bh.Insert(0.5)
    bh.Insert(4.5)

    """
             1
          /     \
         2       3
       /  \     /  \
      4.5  5   6    7
     / 
    4  
    """
    bh.DelMin()

    bh2 = BinaryHeap()
    lst = [3, 7, 9, 5, 0.8, 4]
    for x in lst:
        bh2.Insert(x)
    bh3 = BinaryHeap()
    print(bh3.BuildHeap(lst))
