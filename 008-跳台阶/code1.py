# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        a = 1
        b = 2
        for i in range(2,number):
            a,b = b,a+b
        return b
