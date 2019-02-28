# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odds = []
        evens = []
        for i in array:
            if i&1:
                odds.append(i)
            else:
                evens.append(i)
        array = []
        array.extend(odds)
        array.extend(evens)
        return array
