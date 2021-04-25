
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
    def __init__(self, root):
        self.root = root
        self.size = 0
        pass

    def _put(self, key, val, tnod):
        if tnod is not None:
            if tnod.key > key:
                if tnod.left is not None:
                    self._put(key, val, tnod.left)
                elif tnod.left is None:
                    tnod.left = TreeNode(key=key, val=val, left=None, right=None, parent=tnod)
            elif tnod.key < key:
                if tnod.right is not None:
                    self._put(key, val, tnod.right)
                elif tnod.right is None:
                    tnod.right = TreeNode(key=key, val=val, left=None, right=None, parent=tnod)

    def put(self, key, val):
        """
        troubles:
            1. root:1 right:3的二叉搜索树，插入key为2的节点时应放在root:1的left节点还是right:3的left节点？2
            2. _put函数的功能是什么? _put()函数返回结果如何传回put()函数;
        :param key:
        :param val:
        :return:
        """

        if self.root is None:
            self.root = TreeNode(key=key, val=val, left=None, right=None, parent=None)
        else:
            self._put(key, val, self.root)

        self.size += 1

    def __setitem__(self, key, value):
        return self.put(key, value)

    def _get(self, key, tnode):
        if tnode is not None:
            if tnode.key > key:
                self._get(key, tnode.left)
            elif tnode.key < key:
                self._get(key, tnode.right)
            elif tnode.key == key:          # TODO: tnode.key = 24, tnode.val = 6.2, but return None ???????
                return tnode.val
        else:
            return None

    def get(self, key):
        if self.root is not None:
            res = self._get(key, self.root)
            if res is not None:
                return res
            else:
                raise KeyError('key not exists in the BST')
        else:
            raise KeyError('key not exists in the BST')

    def __getitem__(self, item):
        return self.get(item)

    def delete(self, key):

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

    """
    KeyTree:     1                     
              /     \
             0       3
                    /  \
                   2    12
                    \     \
                     4     24
                      \
                       5
                        \
                         6
    """
    bh4 = TreeNode(1, 0.8, None, None, None)
    bst = BinarySearchTree(bh4)
    bst.put(0, 12.4)
    bst.put(3, 2.4)
    bst.put(2, 9.2)
    bst.put(12, 8.2)
    bst.put(4, 7.2)
    bst.put(24, 6.2)
    bst.put(5, 5.2)
    bst.put(6, 4.2)

    print(bst)
    print(bst[1])
    print(bst[24])
    print(bst[0])
    # print(bst[999])
