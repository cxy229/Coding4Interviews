# -*- coding: utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n=len(array[0])
        col = n-1
        row = 0
        while col >= 0 and row <= n-1:
            if target < array[row][col]:
                col -= 1
            elif target > array[row][col]:
                row += 1
            else:
                return True
        return False
while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(raw_input()))
        array=L[1]
        target=L[0]
        flag = S.Find(target, array)
        if flag:
            print('true')
        else:
            print('false')
    except:
        break
