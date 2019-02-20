# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.Fibonacci(n-1) + self.Fibonacci(n-2))


while True:
    try:
        S=Solution()
        n = eval(raw_input())
        print S.Fibonacci(n)
    except:
        break
