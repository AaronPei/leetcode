# -*- coding: utf-8 -*-
'''
@File    :   Solution.py
@Time    :   2019-02-13 23:32:11
@Author  :   Aaron Pei 
@Desc    :   None
'''

# here put the import lib


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            print(self.list)
            return
        if left < n:
            self._gen(left+1, right, n, result+'(')
            # print(left+1, right, n, result+'(')
        if left > right and right < n:
            self._gen(left, right+1, n, result+')')
            # print(left, right+1, n, result+')')

if __name__ == "__main__":
    S = Solution()
    S.generateParenthesis(3)
