# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a,b = 1,2
            for i in range(2,number):
                a,b = b,a+b
            return b
