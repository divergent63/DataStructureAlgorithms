
def sameCharInWord():
    word1 = 'apple'
    word2 = 'pleap'

    cnt1 = [0]*26
    cnt2 = [0]*26

    same = None

    for i in range(len(word1)):
        pos = ord(word1[i]) - ord('a')
        cnt1[pos] += 1

    for i in range(len(word2)):
        pos = ord(word2[i]) - ord('a')
        cnt2[pos] += 1

    for i in range(len(cnt1)):
        if cnt1[i] != cnt2[i]:
            same = 0
        else:
            same = 1

    print(same)
    return same


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#     def put(y):
#         pass
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
class PrintBinaryTreeSolution:
    def _DropNone(self, lst):
        StayIdx = []
        for i in range(len(lst)):
            if lst[i] != None:
                StayIdx.append(i)
        return [lst[StayIdx[i]] for i in range(len(StayIdx))]

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        CurrentNode = root
        CurrentNodeIniDepth = [root]
        # CurrentNodeIniDepth = [self.root.left, self.root.right]

        PrintLst = [CurrentNode.val]
        CurrentDepthLst = []
        # PrintLst.append([CurrentNode.key, CurrentNode.val])
        while True:
            for i in range(len(CurrentNodeIniDepth)):
                if CurrentNodeIniDepth.count(None) == len(CurrentNodeIniDepth):
                    PrintLst = self._DropNone(PrintLst)
                    return PrintLst
                # PrintLst.append([CurrentNodeIniDepth[i].left.key, CurrentNodeIniDepth[i].left.val]) if CurrentNodeIniDepth[i].left is not None else PrintLst.append([None, None])
                # PrintLst.append([CurrentNodeIniDepth[i].right.key, CurrentNodeIniDepth[i].right.val]) if CurrentNodeIniDepth[i].right is not None else PrintLst.append([None, None])
                if CurrentNodeIniDepth[i]:
                    PrintLst.append(CurrentNodeIniDepth[i].left.val) if CurrentNodeIniDepth[i].left is not None else PrintLst.append(None)
                    PrintLst.append(CurrentNodeIniDepth[i].right.val) if CurrentNodeIniDepth[i].right is not None else PrintLst.append(None)
                else:
                    PrintLst.append(None)
                    PrintLst.append(None)
                # PrintLst.append([CurrentNodeIniDepth[i].left.key, CurrentNodeIniDepth[i].left.val, CurrentNodeIniDepth[i].right.key, CurrentNodeIniDepth[i].right.val])
            for i in range(len(CurrentNodeIniDepth)):
                if CurrentNodeIniDepth[i]:
                    CurrentDepthLst.append(CurrentNodeIniDepth[i].left) if CurrentNodeIniDepth[i].left is not None else CurrentDepthLst.append(None)
                    CurrentDepthLst.append(CurrentNodeIniDepth[i].right) if CurrentNodeIniDepth[i].right is not None else CurrentDepthLst.append(None)
                else:
                    CurrentDepthLst.append(None)
                    CurrentDepthLst.append(None)
            CurrentNodeIniDepth = CurrentDepthLst
            CurrentDepthLst = []


# @param pRoot TreeNode类
# @return TreeNode类
#
import DST_Tree
class Solution:
    def Mirror(self, pRoot):
        # write code here
        print_BT = PrintBinaryTreeSolution()
        pRoot_lst = print_BT.PrintFromTopToBottom(pRoot)
        bt = DST_Tree.BinaryTree(pRoot.val)
        for pRoot_item in pRoot_lst:
            pRoot_item.reverse()
            for i, x in enumerate(pRoot_item):
                if i % 2 == 0:
                    bt.InsertLeft(x)
                else:
                    bt.InsertRight(x)
        return bt


if __name__ == '__main__':
    sameCharInWord()
