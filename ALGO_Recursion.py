"""
递归三要素：
    1. 问题规模减小
    2. 存在结束条件
    3. 必须调用自身 <自相似性>

问题规模缩小的情况：
    1. 链表节点越来越少
    2. 求和、积等问题中因数越来越少，计算式越来越短
    3.

递归 --属于--> 分治策略 --改进--> 贪婪策略
"""

import turtle


def continue_sum(lst):
    print(lst)

    if len(lst) != 1:
        return lst[0] + continue_sum(lst[1:])
    else:
        return lst[0]


def baseTransfer(n, base):
    elem = '0123456789ABCDE'
    if n < base:
        return elem[n]
    else:
        return baseTransfer(n // base, base) + elem[n % base]


class tree():
    def __init__(self):
        # turtle.__init__()
        self.t = turtle.Turtle()
        self.t.left(90)
        self.t.penup()
        self.t.backward(300)
        self.t.pendown()
        self.t.pencolor('green')
        self.t.pensize(2)
        self.drawTree(75, 2)
        self.t.hideturtle()
        turtle.done()

    def drawTree(self, len_, min_):
        if len_ > min_:
            self.t.forward(len_)
            self.t.right(15)
            self.drawTree(len_ - 5, min_)
            self.t.left(30)
            self.drawTree(len_ - 5, min_)
            self.t.right(15)
            self.t.backward(len_)


class sierpinski():
    def __init__(self, n):
        self.color = None
        self.t = turtle.Turtle()
        self.points = {'left': (-400, -300), 'top': (200, 300), 'right': (400, -300)}
        ps = self.points
        self.recursion(n, ps)
        turtle.done()
        pass

    def singleDraw(self, points_in):
        self.t.fillcolor(self.color)
        self.t.penup()
        self.t.goto(points_in['top'])
        self.t.pendown()
        self.t.begin_fill()
        self.t.goto(points_in['left'])
        self.t.goto(points_in['right'])
        self.t.goto(points_in['top'])
        self.t.end_fill()
        pass

    def recursion(self, n, ps):
        color_map = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
        if n < len(color_map):
            self.color = color_map[n]
        else:
            self.color = color_map[n%len(color_map)]
        self.singleDraw(ps)

        if n > 0:           # 结束条件
            # 绘制左下角的三角形
            if n < len(color_map):
                self.color = color_map[n-1]
            else:
                self.color = color_map[n % len(color_map)-1]
            pst = ((ps['top'][0] + ps['left'][0]) / 2, (ps['top'][1] + ps['left'][1]) / 2)
            psr = ((ps['right'][0] + ps['left'][0]) / 2, (ps['right'][1] + ps['left'][1]) / 2)
            psl = ps['left']

            # 调用自身
            self.recursion(
                n - 1,          # 规模减小
                {'top': pst, 'right': psr, 'left': psl}
            )            # self.singleDraw()

            # 绘制顶部的三角形
            if n < len(color_map):
                self.color = color_map[n-1]
            else:
                self.color = color_map[n % len(color_map)-1]
            pst = ps['top']
            psr = ((ps['top'][0] + ps['right'][0]) / 2, (ps['top'][1] + ps['right'][1]) / 2)
            psl = ((ps['top'][0] + ps['left'][0]) / 2, (ps['top'][1] + ps['left'][1]) / 2)

            self.recursion(
                n - 1,
                {'top': pst, 'right': psr, 'left': psl}
            )            # self.singleDraw()

            # 绘制右下角的三角形
            if n < len(color_map):
                self.color = color_map[n-1]
            else:
                self.color = color_map[n % len(color_map)-1]
            pst = ((ps['top'][0] + ps['right'][0]) / 2, (ps['top'][1] + ps['right'][1]) / 2)
            psr = ps['right']
            psl = ((ps['right'][0] + ps['left'][0]) / 2, (ps['right'][1] + ps['left'][1]) / 2)
            self.recursion(
                n - 1,
                {'top': pst, 'right': psr, 'left': psl}
            )
            # self.singleDraw()


class minClassCoins():
    def __init__(self, coinClassLst):
        self.coinClassLst = coinClassLst
        self.coinClassLst.sort()
        # self.maxCoinVal = maxCoinVal
        self.changed_recursion = 0

        pass

    def greedyPolicy(self, maxCoinVal):
        coin = min(max(self.coinClassLst), maxCoinVal)
        coin_match = 0

        changed = 0
        changed_lst = []
        while True:
            # coin *= cnt
            coin_match += coin
            changed += 1
            changed_lst.append(coin)
            if coin_match > maxCoinVal:
                coin_match = coin_match - coin
                del self.coinClassLst[-1]
                coin = min(max(self.coinClassLst), maxCoinVal)
                changed -= 1
                del changed_lst[-1]

            if coin_match == maxCoinVal:
                print(changed_lst)
                return changed

    def recursionCall(self, maxCoinVal):
        """
        TODO: fuck can't understand ...
        :param maxCoinVal:
        :return:
        """
        # coinLst = [c for c in self.coinClassLst if c <= maxCoinVal]
        # coinLst.reverse()
        #
        # if maxCoinVal in self.coinClassLst:
        #     return self.changed_recursion
        # else:
        #     for i, x in enumerate(coinLst):
        #         self.changed_recursion = 1 + self.recursionCall(maxCoinVal-x)
        #         if maxCoinVal - x < 0:
        #             pass
        #         # if maxCoinVal > x:
        #         #     maxCoinVal = maxCoinVal - x
        #         #     self.recursionCall(maxCoinVal)
        #         # elif i < len(self.coinClassLst)-1:
        #         #     self.changed_recursion += 1
        #         #     maxCoinVal = maxCoinVal + x - self.coinClassLst[i+1]
        #         #     # self.recursionCall(maxCoinVal)
        #
        # return self.changed_recursion
        minCoins = maxCoinVal
        if maxCoinVal in self.coinClassLst:
            return 1  # 最小规模，直接返回。
        else:
            for i in [c for c in self.coinClassLst if c <= maxCoinVal]:
                # if i == 5:
                #     print(i)
                numCoins = 1 + self.recursionCall(maxCoinVal - i)  # 调用自身和减少规模。
                if numCoins < minCoins:
                    minCoins = numCoins
        return minCoins

    def dynamicPrograming(self, maxCoinVal):
        memory = [0]*(maxCoinVal+1)
        for cent in range(1, maxCoinVal+1):
            minCoinCount = cent
            for coin in [c for c in self.coinClassLst if c <= cent]:
                if memory[cent-coin] < minCoinCount:           # 试探取不同的coin对最小硬币数目minCoinCount的影响，如果当前记忆memory[cent-coin]小于最小数目，则更新最小数目为当前记忆+1次兑换
                    minCoinCount = memory[cent-coin]+1              # 更新最小数目为当前记忆+1次兑换
            memory[cent] = minCoinCount
        return memory[maxCoinVal]

#
# # 递归解决找零问题v1。
# import time
# start = time.time()
# def recMC(coinValueList, change):
#     minCoins = change
#     if change in coinValueList:
#         return 1  # 最小规模，直接返回。
#     else:
#         for i in [c for c in coinValueList if c <= change]:
#             numCoins = 1 + recMC(coinValueList, change - i)  # 调用自身和减少规模。
#             if numCoins < minCoins:
#                 minCoins = numCoins
#     return minCoins
#
# print(recMC([1, 5, 10, 25], 63))
# end = time.time()
# print(f"运行本递归程序一共用了{end - start}秒。")
# # <<<
# # 6
# # 运行本递归程序一共用了37.6766254901886秒。
# # <<<


if __name__ == '__main__':
    # print(continue_sum([i*2+1 for i in range(2)]))
    # print(baseTransfer(2414, 2))

    # tree()

    # spsk = sierpinski(3)

    print(
        # minClassCoins([1, 5, 10, 21, 25]).greedyPolicy(63),           # wrong answer: 6
        # minClassCoins([1, 5, 10, 25]).greedyPolicy(63),
        # minClassCoins([1, 5, 10, 21, 25]).recursionCall(63),
        # minClassCoins([1, 5, 10, 25]).recursionCall(26)
        minClassCoins([1, 5, 10, 21, 25]).dynamicPrograming(63)
    )
    pass
