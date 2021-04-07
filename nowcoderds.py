# -*- coding: utf-8 -*-
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def PrintTree(root):
    if root == None:
        sys.stdout.write("{}")
        return
    sys.stdout.write("{")
    v = [root]
    c = 0
    none = ""
    while c < len(v):
        if c == 0:
            sys.stdout.write("%d" % v[c].val)
            v.append(v[c].left)
            v.append(v[c].right)
        else:
            if v[c] == None:
                none = none + ",#"
            else:
                sys.stdout.write("%s,%d" % (none, v[c].val))
                none = ""
                v.append(v[c].left)
                v.append(v[c].right)
        c = c + 1
    sys.stdout.write("}")


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def PrintTreeLinkNode(root):
    if root == None:
        sys.stdout.write("{}")
        return
    sys.stdout.write("{[")
    v = []
    label_node_v = []
    if root is not None:
        v.append(root)
        label_node_v.append(root)
    c = 0
    none = ""
    while c < len(v):
        if c == 0:
            sys.stdout.write("%d" % v[c].val)
            v.append(v[c].left)
            v.append(v[c].right)
        else:
            if v[c] == None:
                none = none + ",#"
            else:
                label_node_v.append(v[c])
                sys.stdout.write("%s,%d" % (none, v[c].val))
                none = ""
                v.append(v[c].left)
                v.append(v[c].right)
        c = c + 1
    v = []
    sys.stdout.write("],[")
    for i in range(0, len(label_node_v)):
        if i is not 0:
            sys.stdout.write(",")
        if label_node_v[i].next is not None:
            sys.stdout.write("%d" % label_node_v [i].next.val)
        else:
            sys.stdout.write("#")
    sys.stdout.write("]}")


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def PrintRandomListNode(head):
    if head == None:
        sys.stdout.write("{}")
        return
    current = head
    sys.stdout.write("{")
    while current is not None:
        if current == head:
            sys.stdout.write("%d" % current.label)
        else:
            sys.stdout.write(",%d" % current.label)
        current = current.next

    current = head
    while current is not None:
        if current.random is not None:
            sys.stdout.write(",%d" % current.random.label)
        else:
            sys.stdout.write(",#")
        current = current.next
    sys.stdout.write("}")


if __name__ == '__main__':
    # node1 = TreeNode(1)
    # node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node4 = TreeNode(4)
    # node5 = TreeNode(5)
    # node1.left = node2
    # node1.right = node3
    # node3.left = node4
    # node4.right = node5
    # PrintTree(node1)
    # print('')
    #
    # tlnode1 = TreeLinkNode(1)
    # tlnode2 = TreeLinkNode(2)
    # tlnode3 = TreeLinkNode(3)
    # tlnode4 = TreeLinkNode(4)
    # tlnode5 = TreeLinkNode(5)
    # tlnode1.left = tlnode2
    # tlnode1.right = tlnode3
    # tlnode3.left = tlnode4
    # tlnode4.right = tlnode5
    # tlnode2.next = tlnode3
    # PrintTreeLinkNode(tlnode1)
    # print('')

    rlnode1 = RandomListNode(-1)
    rlnode2 = RandomListNode(8)
    rlnode3 = RandomListNode(7)
    rlnode4 = RandomListNode(-3)
    rlnode5 = RandomListNode(4)
    rlnode1.next = rlnode2
    rlnode2.next = rlnode3
    rlnode3.next = rlnode4
    rlnode4.next = rlnode5
    rlnode1.random = rlnode5
    rlnode2.random = rlnode4
    rlnode5.random = rlnode2
    PrintRandomListNode(rlnode1)
