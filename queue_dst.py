# -*- coding:utf-8 -*-
class stack():
    def __init__(self):
        self.stack_lst = []

    def push(self, item):
        return self.stack_lst.append(item)

    def pop(self):
        return self.stack_lst.pop()

    def peek(self):
        return self.stack_lst[-1]

    def peeki(self, i):
        return self.stack_lst[i]

    def isEmpty(self):
        return len(self.stack_lst) == 0

    def size(self):
        return len(self.stack_lst)

    def min(self):
        if self.stack_lst is not None:
            return min(self.stack_lst)
        else:
            return None


class queue_test():
    # Use two stack to realize queue operations
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def push(self, node):
        # write code here
        return self.s1.push(node)

    def pop(self):
        # return xx
        self.s2 = stack()

        # 反转栈s1并保存为栈s2
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())

        # 返回栈s2被删除的最后一个元素值，即s1的第一个元素值
        result = self.s2.pop()
        # self.s1 = self.s2

        # 将再次反转的栈s2各元素push进已经为空的栈s1
        for i in range(self.s2.size()):
            self.s1.push(self.s2.peeki(self.s2.size() - i - 1))
        return result

    def pop_recursion(self):

        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())

        if self.s2.size() is not 0 and self.s1.isEmpty():
            while not self.s2.isEmpty():
                if self.s1.isEmpty():
                    self.s1.push(self.s2.pop())

            self.pop_recursion()

        return self.s2.pop()


if __name__ == '__main__':
    q = queue_test()
    # print(
    #     q.push(1),
    #     q.push(2),
    #     q.push(3),
    #     q.pop(),
    #     q.pop(),
    #     q.push(4),
    #     q.pop(),
    #     q.push(5),
    #     q.pop(),
    #     q.pop()
    # )
    print(
        q.push(1),
        q.push(2),
        q.push(3),
        q.pop_recursion(),
        # q.pop_recursion(),
        # q.push(4),
        # q.pop_recursion(),
        # q.push(5),
        # q.pop_recursion(),
        # q.pop_recursion()
    )

    pass
