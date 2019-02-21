# -*- coding: utf-8 -*-

# Definition for a binary tree node.


'''
@description: 中序遍历验证，缺点时空间复杂度O(n)
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
        inorder = self.inOrder(root)
        # 调用inOrder按照中序遍历(左中右)获取所有的子节点，再将所得数组去重排序比较。
        return inorder == list(sorted(set(inorder)))

    def inOrder(self, root):
        if root is None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
