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


# class sierpinski():
#     def __init__(self, n):
#         self.t = turtle.Turtle()
#         self.points = {'left': (-200, -100), 'top': (0, 200), 'right': (200, -100)}
#
#         self.singleDraw(color)
#         turtle.done()
#         pass
#
#     def singleDraw(self, color):
#         self.t.fillcolor(color)
#         pass


if __name__ == '__main__':
    # print(continue_sum([i*2+1 for i in range(2)]))
    # print(baseTransfer(2414, 2))

    tree()