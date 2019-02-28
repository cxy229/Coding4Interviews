# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        for i in range(n):
            for j in range(n-1,i,-1):
                if array[j]&1==1 and array[j-1]&1==0:
                    array[j], array[j-1] = array[j-1], array[j]
        return array
