# -*- coding: utf-8 -*-

# Definition for a binary tree node.
'''
@description: 中序遍历验证，空间复杂度O(1)
@param {type} 
@return: 
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    '''
    @description:  左中右去遍历，将每一分支的结果retrun到上一层来处理。画图理解递归。
    @param {type} 
    @return: 
    '''
    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)