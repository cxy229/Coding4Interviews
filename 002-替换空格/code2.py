# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        cnt = 0
        for c in s:
            if c == ' ':
                cnt += 1
        n = len(s) + cnt*2
        new_s = [' ']*n
        i,j = 0,0
        while i<len(s):
            if s[i] != ' ':
                new_s[j] = s[i]
                i += 1
                j += 1
            else:
                new_s[j] = '%'
                new_s[j+1] = '2'
                new_s[j+2] = '0'
                i += 1
                j += 3
        return ''.join(new_s)
