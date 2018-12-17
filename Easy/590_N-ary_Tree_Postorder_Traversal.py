"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        output = []

        while stack:

            node = stack.pop()
            output.append(node.val)
            stack.extend(node.children[:])

        return output[::-1]
