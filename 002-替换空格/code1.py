# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        _s = list(s)
        for i in range(len(_s)):
            if _s[i] == ' ':
                _s[i] = '%20'
        return ''.join(_s)
