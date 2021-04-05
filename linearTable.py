
class linkedListNode(object):  # ListNode继承object中的方法
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def _getData(self):
        return self.data

    def _getNext(self):
        return self.next

    def _setData(self, newData):
        self.data = newData

    def _setNext(self, newNext):
        self.next = newNext


class linkedListOperation():
    def __init__(self):
        self.currentNode = None

    def clear(self):
        return self.currentNode._setNext(None)

    def insert(self, data):
        temp = linkedListNode(data)
        temp._setNext(self.currentNode)
        self.currentNode = temp
        return temp

    def size(self):
        current = self.currentNode
        cnt = 0
        while current != None:
            cnt += 1
            current = current._getNext()
        return cnt

    def search(self, data):
        current = self.currentNode
        found = False
        while current != None and not found:
            if current._getData() == data:
                return current
            else:
                current = current._getNext()
        return found

        # current = self.currentNode
        # found = False
        # while current != None and not found:
        #     if current._getData() == item:
        #         found = True
        #     else:
        #         current = current._getNext()
        # return found

    def remove(self, data):
        previous = None
        current = self.currentNode

        while current != None:
            if current._getData() == data and previous == None:
                previous = current._getNext()
                return previous
            elif current._getData() == data and previous != None:
                previous._setNext(current._getNext())
                return previous
            else:
                previous = current
                current = current._getNext()
        return 'no node like this!'

        # previous = None
        # current = self.currentNode
        #
        # while current != None:
        #     if current._getData() == data and previous != None:
        #         previous._setNext(current._getNext())
        #         return previous
        #     else:
        #         previous = current
        #         current = current._getNext()
        #
        # if previous == None:
        #     previous = current._getNext()
        #     return previous
        # else:
        #     previous._setNext(current._getNext())
        # return 'no node like this!'

    def findKthToTail(self, pHead, k):
        self.currentNode = pHead

        size = self.size()

        cnt = 0
        temp = pHead
        while size - cnt != k and temp != None:
            temp = temp._getNext()
            cnt += 1
        if temp == None:
            return None
        return temp._getData()

    def reverse(self, pHead):
        self.currentNode = pHead

        if pHead != None:
            previous = pHead
            current = previous._getNext()

            while current != None:
                temp = current._getNext()
                current._setNext(pHead)
                previous._setNext(temp)

                pHead = current
                current = temp

        return pHead

    def deleteDuplication(self, pHead):
        # write code here
        #         previous = pHead
        current = pHead
        splitNode_lst = []
        splitVal_lst = []
        while current is not None:
            splitNode_lst.append(current)
            splitVal_lst.append(current._getData())
            current = current._getNext()

        splitVal_lst_n = []
        for i in range(len(splitVal_lst)):
            if splitVal_lst.count(splitVal_lst[i]) == 1:
                splitVal_lst_n.append(splitVal_lst[i])

        if len(splitVal_lst_n) == 0:
            return

        temp = linkedListNode(splitVal_lst_n[0])
        pre = temp
        for i in range(1, len(splitVal_lst_n)):
            if splitVal_lst_n[i - 1] != splitVal_lst_n[i]:
                new = linkedListNode(splitVal_lst_n[i])
                pre._setNext(new)
                pre = pre._getNext()

        return temp

    def insertOrderd(self, pHead, data):
        previous = None
        current = pHead
        inserted = False

        temp = linkedListNode(data)
        if current._getData() > data and previous == None:
            temp._setNext(pHead)
            # pHead = temp          # TODO: 实际效果为 temp = pHead ？？？？？
            return temp

        previous = current
        current = current._getNext()
        while previous is not None and current is not None and not inserted:
            if not current._getData() < data:
                # temp = current
                previous._setNext(temp)
                temp._setNext(current)
                inserted = True
            previous = current
            current = current._getNext()
        if not previous._getData() > data:
            previous._setNext(temp)
        return pHead

    def mergeTwoOrderedList_v2(self, pHead1, pHead2):
        # TODO: cost too many times
        current = pHead2

        while current is not None:
            currentData = current._getData()
            current = current._getNext()

            pHead1 = self.insertOrderd(pHead1, currentData)

        return pHead1

    def mergeTwoOrderedList_v3(self, pHead1, pHead2):
        # TODO:
        current = pHead1
        current2 = pHead2
        previous = None
        inserted = False
        currentData = data

        temp = linkedListNode(data)
        if current2._getData() > data and previous == None:
            # insert pHead2.current2 before head node of pHead1
            temp._setNext(pHead1)
            pHead1 = temp          # TODO: 实际效果为 temp = pHead ？？？？？
            # return temp

        previous = current
        current = current._getNext()
        while current2 is not None and previous is not None and current is not None and not inserted:

            currentData = current2._getData()
            current2 = current2._getNext()

            if not current._getData() < currentData:
                # temp = current
                previous._setNext(temp)
                temp._setNext(current)
                inserted = True
            previous = current
            current = current._getNext()
            # pHead1 = self.insertOrderd(pHead1, currentData)

        if not previous._getData() > currentData:
            previous._setNext(temp)

        return pHead1

    def mergeTwoOrderedList(self, pHead1, pHead2):
        # write code here
        temp1_previous = None
        temp1_previous2 = None
        temp1 = pHead1
        temp2 = pHead2
        while temp1 != None and temp2 != None:
            if temp1._getData() < temp2._getData():
                # insert temp2.val behind temp1.val in temp1
                temp_temp1 = temp1._getNext()
                temp1._setNext(temp2)

                temp_temp2 = temp2._getNext()
                temp2._setNext(temp_temp1)

                temp1_previous = temp1
                temp1 = temp_temp1
                temp2 = temp_temp2
            else:
                # insert temp2.val before temp.val in temp1
                if temp1_previous is not None:
                    temp1_previous = temp1_previous._getNext()
                    # temp_temp1 = temp1._getNext()
                    temp_temp2 = temp2._getNext()
                    temp2._setNext(temp1)

                    temp1_previous._setNext(temp2)          # 执行完后pHead会随之改变

                    # temp2._setNext(temp_temp1)

                    # temp1_previous = temp1
                    # temp1 = temp_temp1
                    temp2 = temp_temp2

                else:
                    # TODO
                    # temp_temp1 = temp1._getNext()
                    # temp_temp2 = temp2._getNext()
                    temp2._setNext(pHead1)
                    pHead1 = temp2
                    # temp1 = temp_temp1
                    # temp2 = temp_temp2
                    temp1_previous = temp2
        # if temp1 == None:
        #     temp1_previous._setNext(temp2)
        return pHead1

    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        输入两个链表，找出它们的第一个公共结点。
        TODO: input: {1,2,3},{4,5},{6,7} <{1,2,3,6,7} and {4,5,6,7}>; expect: {6,7}; actual: {}  ?????
        TODO: reason: must reach the common node at same time
        :param pHead1:
        :param pHead2:
        :return:
        """
        # write code here
        current2 = pHead2
        current1 = pHead1
        if current1 is None or current2 is None:
            return
        ph1Val_lst = []
        ph1Nod_lst = []
        ph2Val_lst = []
        ph2Nod_lst = []
        while current1 is not None:
            ph1Val_lst.append(current1._getData())
            ph1Nod_lst.append(current1)
            current1 = current1._getNext()

        while current2 is not None:
            ph2Val_lst.append(current2._getData())
            ph2Nod_lst.append(current2)
            current2 = current2._getNext()

        for i, x in enumerate(ph1Val_lst):
            if x in ph2Val_lst:
                return ph1Nod_lst[i]
            # else:
            #     return

        # for i, x in enumerate(ph2Val_lst):
        #     if x in ph1Val_lst:
        #         return ph2Nod_lst[i]
        #     else:
        #         return

# # l1 = linkedListNode(9)
# l1_op = linkedListOperation()
# for data in [1, 8, 4, 11, 7]:
#     l1 = l1_op.insert(data)
#     # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# print('\n', l1, l1.data, l1.next, '\n', l1.next.data, l1.next.next, '\n', l1_op.size(), l1_op.search(4))
# print(l1_op.size(), l1_op.search(1), l1_op.search(8), l1_op.search(4), l1_op.search(11), l1_op.search(7), l1_op.search(111))
# print(l1_op.size(), l1_op.remove(3), l1_op.remove(1), l1_op.remove(8), l1_op.remove(7))
# print(l1_op.reverse({}), l1_op.reverse(l1))
# print(l1_op.findKthToTail(l1, 4), l1_op.findKthToTail(l1, 12))

# # l1 = linkedListNode(9)
# l111_op = linkedListOperation()
# for data in [200, 4, 1]:
#     l11 = l111_op.insert(data)
#     # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# print(l111_op.insertOrderd(l11, 18)._getNext()._getNext()._getData())
#
# l111_op.clear()
# l112_op = linkedListOperation()
# for data in [200, 18, 4]:
#     l11 = l112_op.insert(data)
#     # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# l112 = l112_op.insertOrderd(l11, 1)
# print(l112_op.insertOrderd(l11, 1)._getData())
#
# l2_op = linkedListOperation()
# for data in [91, 19, 9, 5, 2]:
#     l12 = l2_op.insert(data)
#     # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())

# print('\n', l1, l1.data, l1.next, '\n', l1.next.data, l1.next.next, '\n', l1_op.size(), l1_op.search(4))
# print(l1_op.size(), l1_op.search(1), l1_op.search(8), l1_op.search(4), l1_op.search(11), l1_op.search(7), l1_op.search(111))
# print(l1_op.size(), l1_op.remove(3), l1_op.remove(1), l1_op.remove(8), l1_op.remove(7))
# print(l1_op.reverse({}), l1_op.reverse(l1))
# print(l1_op.mergeTwoOrderedList(l11, l12))


# l112_op = linkedListOperation()
# for data in [5, 3, 1]:
#     l11 = l112_op.insert(data)
#     # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# # print(l112_op.insertOrderd(l11, 1)._getData())
#
# l2_op = linkedListOperation()
# for data in [6, 4, 2]:
#     l12 = l2_op.insert(data)
    # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# print(l2_op.mergeTwoOrderedList_v2(l11, l12))
# print(l2_op.mergeTwoOrderedList_v3(l11, l12))


# l112_op = linkedListOperation()
# for data in [7, 6, 3, 2, 1]:
#     l11 = l112_op.insert(data)
#     # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# # print(l112_op.insertOrderd(l11, 1)._getData())
#
# l2_op = linkedListOperation()
# for data in [7, 6, 5, 4]:
#     l12 = l2_op.insert(data)
# print(l2_op.FindFirstCommonNode(l11, l12))

l112_op = linkedListOperation()
# for data in [7, 6, 4, 4, 3, 3, 2, 1]:
for data in [2, 1, 1, 1, 1]:
    l11 = l112_op.insert(data)
    # print(l1_op.add(data)._getData(), l1_op.add(data)._getNext())
# print(l112_op.insertOrderd(l11, 1)._getData())
print(l112_op.deleteDuplication(l11))