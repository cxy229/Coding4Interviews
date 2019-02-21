# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [0]*(number+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,number+1):
            for j in range(i):
                dp[i] += dp[j]
        return dp[number]
