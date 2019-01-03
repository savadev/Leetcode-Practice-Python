# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])

        i = length // 2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i + 1:])
        return root


