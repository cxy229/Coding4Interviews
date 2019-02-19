# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        for i in range(len(rotateArray)-1,0,-1):
            if rotateArray[i-1]>rotateArray[i]:
                return rotateArray[i]
        return rotateArray[0]
