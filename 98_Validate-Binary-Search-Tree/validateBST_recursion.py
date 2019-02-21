# -*- coding: utf-8 -*-

# Definition for a binary tree node.


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


    '''
    @description: 递归遍历验证。
                  遍历左子树，始终记录左侧最大值,以此作为root的下界。
                  遍历右子树，始终记录右侧最小值，以此作为root的上界。
    @param  传入min，max 上下界
    @return: 
    '''
    def isValidate(self, root, min, max):
        if root is None:
            return True
        if max and root.val >= max:
            return False
        if min and root.val <= min:
            return False
        return self.isValidate(root.left, min, root.val) and self.isValidate(root.right, root.val, max)
