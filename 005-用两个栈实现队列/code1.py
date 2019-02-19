# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sta1 = []
        self.sta2 = []
    def push(self, node):
        # write code here
        self.sta1.append(node)
    def pop(self):
        # return xx
        if len(self.sta2)==0:
            if len(self.sta1)==0:
                return None
            while len(self.sta1):
                self.sta2.append(self.sta1.pop())
            return self.sta2.pop()
        else:
            return self.sta2.pop()
