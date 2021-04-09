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
    def __init__(self, coinClassLst, maxCoinVal):
        self.coinClassLst = coinClassLst
        self.coinClassLst.sort()
        self.maxCoinVal = maxCoinVal

        pass

    def greedyPolicy(self):
        coin = min(max(self.coinClassLst), self.maxCoinVal)
        coin_match = 0

        changed = 0
        while True:
            # coin *= cnt
            coin_match += coin

            if coin_match > self.maxCoinVal:
                coin_match = coin_match - coin
                changed += 1
                del self.coinClassLst[-1]
                coin = min(max(self.coinClassLst), self.maxCoinVal)

            if coin_match == self.maxCoinVal:
                return changed

        pass

    def recursionCall(self):

        pass


if __name__ == '__main__':
    # print(continue_sum([i*2+1 for i in range(2)]))
    # print(baseTransfer(2414, 2))

    # tree()

    # spsk = sierpinski(8)

    print(
        minClassCoins([1, 5, 10, 25], 63).greedyPolicy()
    )
    pass
