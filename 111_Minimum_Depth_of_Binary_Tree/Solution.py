# -*- coding: utf-8 -*-
'''
@File    :   Solution.py
@Time    :   2019-02-02 16:36:02
@Author  :   Aaron Pei 
@Desc    :   分治和DFS
             最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
'''

# here put the import lib

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        # divide and conquer
        leftMin = self.minDepth(root.left)
        rightMin = self.minDepth(root.right)
        
        if leftMin==0 or rightMin==0:
            return leftMin + rightMin +1
        else:
            return min(leftMin, rightMin)+1
