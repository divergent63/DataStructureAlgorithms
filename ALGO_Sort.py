import time


class sortMethod():
    def __init__(self, lst):
        self.lst = lst
        self.mergeSortRes = []
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

    def insertionSort(self, start=0, gap=1):
        """
        去纸上写 ！！
        :return:
        """
        for i in range(start+gap, len(self.lst), gap):
            currentVal = self.lst[i]
            currentPos = i
            while currentPos >= gap:
                if self.lst[currentPos-gap] > currentVal:
                    self.lst[currentPos] = self.lst[currentPos-gap]
                    self.lst[currentPos - gap] = currentVal
                currentPos -= gap
        return self.lst

    def shellInsertionSort(self, lst, start, gap):
        for j in range(start + gap, len(lst), gap):
            curVal = lst[j]
            curPos = j

            while curPos >= gap and lst[curPos - gap] > curVal:
                lst[curPos] = lst[curPos - gap]
                curPos = curPos - gap
            lst[curPos] = curVal

    def shellSort(self):
        gap = len(self.lst) // 2
        while gap > 0:

            for i in range(gap):

                # self.lst = self.insertionSort(start=i, gap=gap)
                self.insertionSort(i, gap)
            # print(gap, self.lst)
            gap = gap // 2

        return self.lst

    def RecurrsionAndMerge(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            left = lst[:(len(lst)//2)]
            right = lst[(len(lst)//2):]
            left_sorted = self.RecurrsionAndMerge(left)
            right_sorted = self.RecurrsionAndMerge(right)

            merged = []
            while left_sorted and right_sorted:
                if left_sorted[0] > right_sorted[0]:
                    merged.append(right_sorted.pop(0))
                else:
                    merged.append(left_sorted.pop(0))

            merged.extend(left_sorted if left_sorted else right_sorted)
            return merged

    def mergeSort(self):

        # if len(self.lst) <= 1:
        #     return self.lst
        # else:

        # 1. 递归； 2. 合并
        return self.RecurrsionAndMerge(self.lst)

    def quickSort(self):

        pass


if __name__ == '__main__':
    lst = [1, 3, 2, 16, 7, 11, 5]
    # lst = []

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


    # # 3.524892807006836
    # start3 = time.time()
    # [sortMethod(lst).insertionSort() for _ in range(int(10e5))]
    # print(sortMethod(lst).insertionSort())
    # end3 = time.time()

    # # 7.26346230506897
    # start4 = time.time()
    # [sortMethod(lst).shellSort() for _ in range(int(10e5))]
    # print(sortMethod(lst).shellSort())
    # end4 = time.time()

    # 9.529287576675415
    start5 = time.time()
    # [sortMethod(lst).mergeSort() for _ in range(int(10e5))]
    print(sortMethod(lst).mergeSort())
    end5 = time.time()

    print(

        # end1 - start1,
        # end2 - start2,
        # end3 - start3,
        # end4 - start4,
        end5 - start5
    )
    pass

