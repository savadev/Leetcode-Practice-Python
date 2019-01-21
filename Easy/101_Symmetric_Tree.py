# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.check(root.left, root.right)

    def check(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_2(object):
    def isSameTree_2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        elif p is not None and q is not None:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree_2(p.left, q.left) and self.isSameTree_2(p.right, q.right)
        else:
            return False
