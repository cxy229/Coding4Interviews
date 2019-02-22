# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        rst = 1
        if exponent<0:
            exponent = -exponent
            base = 1.0/base
        while exponent:
            if exponent&1:
                rst *= base
            base *= base
            exponent = exponent>>1
        return rst
