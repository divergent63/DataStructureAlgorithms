
class binarySearch():
    def __init__(self, itemToBeSearched):
        self.found = False
        self.itemToBeSearched = itemToBeSearched
        pass

    def recursionSearch(self, subLst):
        """
        查找self.itemToBeSearched是否处于subLst中。
        1. 输入输出见param和return
        2. 基本结束条件：a). subLst只剩一个元素且元素与self.itemToBeSearched相等(已找到);    b). subLst被二分为[](不存在)
        3. 递推关系: found = recursionSearch(subLst[half_length])
        :param subLst:二分后的目标列表 ; self.itemToBeSearched:待查找目标值
        :return:self.found，表示是否找到的bool值
        """
        if len(subLst) == 0:
            self.found = False
        elif len(subLst) ==1:
            if self.itemToBeSearched == subLst[int(len(subLst)/2)]:
                self.found = True
            # else:
            #     self.found = False
        else:
            # subLst = subLst[0:int(len(subLst)/2)]
            self.found = self.recursionSearch(subLst[0:int(len(subLst)/2)])
            if not self.found:
                self.found = self.recursionSearch(subLst[int(len(subLst) / 2):])
            # else:
            #     # subLst = subLst[int(len(subLst)/2)-1:-1]
            #     self.found = False
        return self.found


if __name__ == '__main__':
    print(binarySearch(7).recursionSearch([1, 2, 3, 4, 5, 60]))

    pass




