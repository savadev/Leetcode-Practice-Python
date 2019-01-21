# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        depth = 0
        list = [root]

        while list:
            depth += 1
            for i in range(len(list)):
                if list[0].left:
                    list.append(list[0].left)

                if list[0].right:
                    list.append(list[0].right)

                del list[0]

        return depth
