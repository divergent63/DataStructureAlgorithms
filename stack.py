
class stack():
    def __init__(self):
        self.stack_lst = []

    def push(self, item):
        return self.stack_lst.append(item)

    def pop(self):
        return self.stack_lst.pop()

    def peek(self):
        return self.stack_lst[-1]

    def isEmpty(self):
        return len(self.stack_lst) == 0

    def size(self):
        return len(self.stack_lst)


def simpleTest():
    s = stack()

    print(s.isEmpty())

    [s.push(i) for i in range(6)]

    print(s.isEmpty(), s.size())


def parenthesesMatching(str_):
    """
    USAGE:     print('\n', parenthesesMatching('{(())(()()()())[]}'), '\n', parenthesesMatching('{(())(()()([)]())[]}'))
    HTML/XML validation and operation
    :param str_:
    :return:
    """
    def matches(a, b):
        return '{[('.index(a) == '}])'.index(b)

    s = stack()
    for s_ in str_:
        if s_ in '{[(':
            s.push(s_)
        else:
            if s.isEmpty():
                return 'not match!'
            else:
                if matches(s.peek(), s_):
                    s.pop()

    if s.isEmpty():
        return 'match!'
    else:
        return 'not match!'


def baseTransfer(num, base):
    """
    USAGE:    print(baseTransfer(25, 2), baseTransfer(25, 16))
    convert any 10 base number to any base (!>16) number
    :param num:
    :param base:
    :return:
    """
    elem = '0123456789ABCDE'
    s = stack()
    while num > 0:
        s.push(num % base)
        num = num // base

    num_new_str = ''
    while not s.isEmpty():
        num_new_str = num_new_str + elem[s.pop()]
    return num_new_str


def suffixVal(eq_str):
    storage = stack()
    eq_lst = list(eq_str)
    es_num_ = 0

    for es in eq_lst:
        try:
            es_num = int(es)

            storage.push(es_num)
        except ValueError:
            if es == '+':
                a1 = storage.pop()
                a2 = storage.pop()
                es_num_new = a1 + a2
                storage.push(es_num_new)

            elif es == '*':
                a1 = storage.pop()
                a2 = storage.pop()
                es_num_new = a1 * a2
                storage.push(es_num_new)

            elif es == '-':
                a1 = storage.pop()
                a2 = storage.pop()
                es_num_new = a1 - a2
                storage.push(es_num_new)

            elif es == '/':
                a1 = storage.pop()
                a2 = storage.pop()
                es_num_new = a1 / a2
                storage.push(es_num_new)
    return es_num_new


if __name__ == '__main__':
    print(suffixVal('34*5+'), suffixVal('345*+'), suffixVal('345*+6-'))
    pass
