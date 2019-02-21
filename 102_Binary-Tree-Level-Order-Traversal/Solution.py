# -*- coding: utf-8 -*-
'''
@File    :   Solution.py
@Time    :   2019/02/02 13:34:13
@Author  :   Aaron Pei 
@Desc    :   None
'''

# here put the import lib
import collections
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :desc: BFS 遍历
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = collections.deque()  # collections集合模块，声明一个双向队列
        queue.append(root)
        # isVisted = set(root) 如果BFS遍历图的话，需要一个set来统计遍历过的元素，以防形成死循环。
        while queue:
            level_size = len(queue)
            cur_level = []
            for _ in range(level_size):
                node = queue.popleft()
                cur_level.append(node.val)
                # 将下一层的所有node 都加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(cur_level)
        return result

    def levelOrder1(self, root):
        '''
        @description: DFS遍历-递归方式
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        '''
        @description: 深度遍历一个分支，并将该该分支的node添加到对应的层
        @param {type} 
        @return: 
        '''
        if not node:
            return
        # 为每一层在result中添加一个数组
        if len(self.result) < level+1:
            self.result.append([])
        self.result[level].append(node.val)
        self._dfs(node.left, level+1)
        self._dfs(node.right, level+1)


if __name__ == "__main__":
    T3 = TreeNode(3)
    T9 = TreeNode(9)
    T20 = TreeNode(20)
    T15 = TreeNode(15)
    T7 = TreeNode(7)
    T3.left = T9
    T3.right = T20
    T20.left = T15
    T20.right = T7

    queue = collections.deque()
    queue.append(T3)
    print(Solution().levelOrder1(T3))
