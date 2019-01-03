# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node != None and node.next != None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
