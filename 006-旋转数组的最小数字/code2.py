# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
         # write code here
        if not rotateArray:
            return 0
        low = 0
        high = len(rotateArray) - 1
        if rotateArray[low]<rotateArray[high]:
            return rotateArray[low]
        while True:
            mid = (low + high) // 2
            if rotateArray[mid] >= rotateArray[low]:
                low = mid
            else:
                high = mid
            if rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]
