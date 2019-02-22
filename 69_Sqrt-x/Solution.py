# -*- coding: utf-8 -*-
'''
@File    :   Solution.py
@Time    :   2019-02-22 12:41:55
@Author  :   Aaron Pei 
@Desc    :   二分法和牛顿迭代法
'''

# here put the import lib


class Solution(object):
    def mySqrt(self, x):
        """
        @description: 二分法
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l, r, res = 1, x, None
        while l <= r:
            m = (l+r)/2
            if m == x/m:
                return m
            elif m > x/m:
                r = m-1
            else:
                l = m+1
                res = m
        return res

    def mySqrt(self, x):
        """
        @description: 牛顿迭代法
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r+x/r)/2
        return r
