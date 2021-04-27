
"""
See also DST_NonLinearTable.py

二叉树
二叉堆 （ 平衡： 满二叉树 --> 完全二叉树 ）
二叉搜索树
AVL树
"""
import random

# from DST_NonLinearTable import TreeNode


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
        # TreeNode.__init__(key)
        self.key = key
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent


class BinarySearchTree():
    def __init__(self, root):
        self.root = root
        self.size = 0

    def PreOrder(self, node):
        if node:
            print(node.key, node.val)
            self.PreOrder(node.left)
            self.PreOrder(node.right)

    def MidOrder(self, node):
        if node:
            self.MidOrder(node.left)
            print(node.key, node.val)
            self.MidOrder(node.right)

    def PostOrder(self, node):
        if node:
            self.PostOrder(node.left)
            self.PostOrder(node.right)
            print(node.key, node.val)

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

    def Put(self, key, val):
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
        return self.Put(key, value)

    def _get(self, key, tnode):
        if tnode is not None:
            if tnode.key > key:
                self._get(key, tnode.left)
            elif tnode.key < key:
                self._get(key, tnode.right)
            elif tnode.key == key:          # TODO: tnode.key = 24, tnode.val = 6.2, but return None ???????
                return tnode
        else:
            return None

    def get(self, key):
        if self.root is not None:
            res = self._get(key, self.root)         # TODO: tnod in self._get() is not None, but res is None ??????
            if res is not None:
                return res.val
            else:
                raise KeyError('Key not exists in the BST')
        else:
            raise KeyError('Key not exists in the BST')

    def GetUnrecNode(self, key):
        pNode = self.root
        if pNode:
            # while pNode.right and pNode.left:
            while True:
                if pNode.key < key:
                    pNode = pNode.right
                elif pNode.key > key:
                    pNode = pNode.left
                elif pNode and pNode.key == key:
                    return pNode
                else:
                    return
        else:
            return

    def GetUnrec(self, key):
        pNode = self.root
        if pNode:
            # while pNode.right and pNode.left:
            while True:
                if pNode.key < key:
                    pNode = pNode.right
                elif pNode.key > key:
                    pNode = pNode.left
                elif pNode and pNode.key == key:
                    return pNode.val
                else:
                    raise KeyError('Key not exists in the BST')
        else:
            raise KeyError('Key not exists in the BST')

    def __getitem__(self, item):
        # return self.get(item)
        return self.GetUnrec(item)

    def _DeleteSituation1(self, node):
        # node左右子树均不存在
        # node.parent = None
        if node.parent.left and node.key == node.parent.left.key:
            node.parent.left = None
        elif node.parent.right and node.key == node.parent.right.key:
            node.parent.right = None
        self.size -= 1
        return

    def _DeleteSituation2(self, node):
        # node左子树不存在
        if node.key == node.parent.right.key:
            node.parent.right = node.right
        elif node.key == node.parent.left.key:
            node.parent.left = node.right
        self.size -= 1
        return

    def _DeleteSituation3(self, node):
        # node右子树不存在
        if node.key == node.parent.right.key:
            node.parent.right = node.left
        elif node.key == node.parent.left.key:
            node.parent.left = node.left
        self.size -= 1
        return

    def _DeleteSituation4(self, node):
        # node左右子树均存在
        # 遍历待删除节点的右子节点的左子树直到左子叶节点，将待删除节点替换为该左子叶节点
        node_right = node.right
        while node_right.left:
            node_right = node_right.left
        if node.parent:
            if node.key == node.parent.right.key:
                tmp = node
                node.parent.right = node_right
                node_right.right = tmp
                self._DeleteSituation1(node_right)
                self.size -= 1
            elif node.key == node.parent.left.key:
                tmp = node
                node.parent.right = node_right
                node_right.right = tmp
                self._DeleteSituation1(node_right)
                self.size -= 1
        else:           # node.parent 不存在，即node为根节点
            # node_right.left = node.left
            # node_right.right = node.right
            # node_right.parent = None
            node.key = node_right.key
            node.val = node_right.val
            node_right.parent = None
            self.size -= 1
        return

    def delete(self, key):
        """
        1. node = _get(key)
        2.
            ds1: 不存在任意子树;
            ds2: 不存在左子树;
            ds3: 不存在右子树;
            ds4: 左右子树均存在.
        :param key:
        :return:
        """
        node = self.GetUnrecNode(key)
        if node:
            if node.left is None and node.right is None:            # ds1
                self._DeleteSituation1(node)
            elif node.left is None and node.right is not None:          # ds2
                self._DeleteSituation2(node)
            elif node.left is not None and node.right is None:          # ds3
                self._DeleteSituation3(node)
            elif node.left is not None and node.right is not None:          # ds4
                self._DeleteSituation4(node)
        else:
            print('Key not exists in the BST, can not delete')
        return

    def draw(self):

        pass


class AVLTree(TreeNode):
    """
    旋转操作：
        0. “*子树的*子树导致了AVL树不平衡”：“*旋”
        1. 右右：左旋
        2. 左左：右旋
        3. 左右：左右（旋）
        4. 右左：右左（旋）
    """
    def __init__(self, key, val):
        TreeNode.__init__(self, key, val, None, None, None)
        self.BalanceFactor = 0
        pass


if __name__ == '__main__':
    # bt = BinaryTree(1).InsertLeft(3).InsertLeft(2).InsertRight(1.5)
    # # print(bt.GetLeftChild().GetRootVal())
    # print(bt.preorder(bt))

    # """
    #          0.5
    #        /     \
    #      1         3
    #    /  \      /   \
    #   2    5    6     7
    #  / \
    # 4  4.5
    # """
    # bh = BinaryHeap()
    # bh.DelMin()
    # [bh.Insert(i) for i in range(1, 8)]
    # bh.Insert(0.5)
    # bh.Insert(4.5)
    #
    # """
    #          1
    #       /     \
    #      2       3
    #    /  \     /  \
    #   4.5  5   6    7
    #  /
    # 4
    # """
    # bh.DelMin()
    #
    # bh2 = BinaryHeap()
    # lst = [3, 7, 9, 5, 0.8, 4]
    # for x in lst:
    #     bh2.Insert(x)
    # bh3 = BinaryHeap()
    # print(bh3.BuildHeap(lst))
    #
    # """
    # KeyTree:     1
    #           /     \
    #          0       3
    #                 /  \
    #                2    12
    #                 \     \
    #                  4     24
    #                   \
    #                    5
    #                     \
    #                      6
    # """
    # bh4 = TreeNode(1, 0.8, None, None, None)
    # bst = BinarySearchTree(bh4)
    # bst.put(0, 12.4)
    # bst.put(3, 2.4)
    # bst.put(2, 9.2)
    # bst.put(12, 8.2)
    # bst.put(4, 7.2)
    # bst.put(24, 6.2)
    # bst.put(5, 5.2)
    # bst.put(6, 4.2)
    #
    # print(bst)
    # bst.mid_order(bst.root)
    # print()
    # bst.pre_order(bst.root)
    # print()
    # bst.post_order(bst.root)
    # print(bst[1])
    # # print(bst[24])
    # # print(bst[0])
    # # print(bst[999])

    lst_k = list(range(1, 501, 2))
    random.shuffle(lst_k)
    lst_v = [random.gauss(0, 1) for _ in range(len(lst_k))]

    bh5 = TreeNode(3, random.gauss(0, 1), None, None, None)
    bst = BinarySearchTree(bh5)
    for i, k in enumerate(lst_k):
        # bst.Put(k, lst_v[i])
        bst[k] = lst_v[i]

    # bst.MidOrder(bst.root)

    # print(bst[3])
    # print(bst.get(113))           # TODO
    # print(bst.GetUnrec(113), bst[115])

    print()
    # bst.delete(1)
    # bst.delete(11)
    bst.delete(3)
    print()

