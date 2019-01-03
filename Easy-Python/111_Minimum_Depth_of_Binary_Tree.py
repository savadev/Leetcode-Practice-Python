# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        elif root.right is None and root.left is not None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))

    def minDepth_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = [root]
        depth = 0

        while q:
            depth += 1
            for i in range(len(q)):
                if not q[0].left and not q[0].right:
                    return depth
                elif q[0].left and (not q[0].right):
                    q.append(q[0].left)
                elif q[0].right and (not q[0].left):
                    q.append(q[0].right)
                else:
                    q.append(q[0].left)
                    q.append(q[0].right)
                del q[0]

        return depth

