# -*- coding: utf-8 -*-
'''
@File    :   Solution.py
@Time    :   2019-02-02 16:35:42
@Author  :   Aaron Pei 
@Desc    :   分治和DFS遍历
'''

# here put the import lib

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
