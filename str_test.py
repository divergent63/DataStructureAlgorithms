#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
class Solution:
    def match(self, str, pattern):
        # write code here
        str_lst = list(str)
        pattern_lst = list(pattern)

        if '*' not in pattern_lst and '.' not in pattern_lst:
            if str == pattern:
                return True
            elif str != pattern:
                return False

        if len(str_lst) == 0 and len(pattern_lst) != 0 and '*' not in pattern_lst:
            return False
        elif len(str_lst) == 0 and len(pattern_lst) != 0 and '*' in pattern_lst:
            return True

        if len(str_lst) == len(pattern_lst):
            while pattern_lst:
                if pattern_lst[0] != '.' and pattern_lst[0] != '*' and str_lst[0] == pattern_lst[0]:
                    str_lst.pop(0)
                    pattern_lst.pop(0)
                elif pattern_lst[0] == '.' or pattern_lst[0] == '*':
                    str_lst.pop(0)
                    pattern_lst.pop(0)
                else:
                    return False
            return True
        elif len(str_lst) != len(pattern_lst) and '.' in pattern_lst:
            if '*' in pattern_lst:
                return True
            else:
                return False
        else:
            str_lst.reverse()
            pattern_lst.reverse()
            while pattern_lst:
                if pattern_lst[0] != '.' and pattern_lst[0] != '*' and str_lst[0] == pattern_lst[0]:
                    str_lst.pop(0)
                    pattern_lst.pop(0)
                #################TODO#############################################
                #                 elif pattern_lst[0] == '*':
                #                     while len(pattern_lst) != len(str_lst)+1:
                #                         tmp = pattern_lst.pop(1)
                #                         if tmp != pattern_lst[1]:
                #                             if len(pattern_lst) <= 1:
                #                                 return False
                #                     pattern_lst.pop(0)
                #                     if pattern_lst == str_lst:
                #                         return True
                #################TODO#############################################
                else:
                    return False
            return True