# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        rst = 1
        if exponent<0:
            exponent = -exponent
            base = 1.0/base
        for i in range(exponent):
            rst *= base
        return rst
