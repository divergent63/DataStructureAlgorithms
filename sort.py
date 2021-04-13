import time


class sortMethod():
    def __init__(self, lst):
        self.lst = lst

        pass

    def bubbleSort(self):

        for i in range(len(self.lst)):
            for j in range(len(self.lst)-1, i, -1):
                if self.lst[j] < self.lst[i]:
                    temp = self.lst[j]
                    self.lst[j] = self.lst[i]
                    self.lst[i] = temp

        return self.lst

    def selectionSort(self):

        for i in range(len(self.lst)):
            tmpLst = []
            for j in range(len(self.lst)-1, i, -1):
                if self.lst[j] < self.lst[i]:
                    temp2 = self.lst[j]
                    tmpLst.append([j, self.lst[j]])
            temp1 = self.lst[i]
            if len(tmpLst) != 0:
                self.lst[i] = tmpLst[-1][1]
                self.lst[tmpLst[-1][0]] = temp1
        return self.lst

    def insertionSort(self):
        """
        去纸上写 ！！
        :return:
        """
        for i in range(1, len(self.lst)):
            currentVal = self.lst[i]
            currentPos = i
            while currentPos > 0:
                if self.lst[currentPos-1] > currentVal:
                    self.lst[currentPos] = self.lst[currentPos-1]
                    self.lst[currentPos - 1] = currentVal
                currentPos -= 1
        return self.lst


if __name__ == '__main__':
    lst = [1, 3, 2, 16, 7, 11]

    # # 4.67067289352417
    # start1 = time.time()
    # [sortMethod(lst).bubbleSort() for _ in range(int(10e5))]
    # print(sortMethod(lst).bubbleSort())
    # end1 = time.time()

    # # 5.8392486572265625
    # start2 = time.time()
    # [sortMethod(lst).selectionSort() for _ in range(int(10e5))]
    # print(sortMethod(lst).selectionSort())
    # end2 = time.time()


    # 3.524892807006836
    start3 = time.time()
    [sortMethod(lst).insertionSort() for _ in range(int(10e5))]
    print(sortMethod(lst).insertionSort())
    end3 = time.time()

    print(
        # end1 - start1,
        # end2 - start2
        end3 - start3
    )
    pass

