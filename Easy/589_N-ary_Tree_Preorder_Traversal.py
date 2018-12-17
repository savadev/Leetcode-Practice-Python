"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
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
            stack.extend(node.children[::-1])
            # stack 后进先出
            # list.extend 和 list.append 区别

        return output
