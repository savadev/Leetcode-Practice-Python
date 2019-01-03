# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        result.append([root.val])

        q = []
        q.append(root)

        while q:
            q_inner = []
            for i in range(len(q)):

                if q[0].left:
                    q.append(q[0].left)
                    q_inner.append(q[0].left.val)
                if q[0].right:
                    q.append(q[0].right)
                    q_inner.append(q[0].right.val)

                del q[0]

            if q_inner != []:
                result.insert(0, q_inner)

        return result