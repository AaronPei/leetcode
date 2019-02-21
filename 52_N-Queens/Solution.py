# -*- coding: utf-8 -*-
'''
@File    :   Solution.py
@Time    :   2019-02-16 15:35:33
@Author  :   Aaron Pei 
@Desc    :   N 皇后问题，给定N，输出**有多少种**解决方案。
             DFS每一行，循环每一列。在循环中针对该行、该列的数字判断是否符合条件。符合则进入下一行。
             符合条件：每个皇后的行、列、撇、捺上都是攻击范围，不能放其它皇后。
                     撇上i+j=C(一个常数)，捺上i-j=C(一个常数)，用一个set来记录
'''

# here put the import lib


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        self.result = 0
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.dfs(0, n, [])

        return self.result

    def dfs(self, row, n, cur_res):
        if row >= n:
            self.result = self.result+1
            return

        for col in range(n):
            # 判断该row，该col是否违法，违法则continue
            if col in self.cols or col+row in self.pie or col-row in self.na:
                continue
            # 找到合适的(row,col)记录
            self.cols.add(col)
            self.pie.add(col+row)
            self.na.add(col-row)
            # 进入下一行
            self.dfs(row+1, n, cur_res+[col])
            # 清空记录
            self.cols.remove(col)
            self.pie.remove(col+row)
            self.na.remove(col-row)


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))
