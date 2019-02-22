# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        for i in range(32):
            if n&1:
                cnt += 1
            n = n>>1
        return cnt
