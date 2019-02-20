# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a = 0
        b = 1
        for i in range(1,n):
            t = b
            b = a+b
            a = t
        return b
