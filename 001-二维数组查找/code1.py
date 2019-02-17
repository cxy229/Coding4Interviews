# -*- coding: utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n=len(array[0])
        for i in range(n):
            low = 0
            high = n-1
            while(low<=high):
                mid = (low+high)//2
                if target < array[i][mid]:
                    high = mid - 1
                elif target > array[i][mid]:
                    low = mid + 1
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
