# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        p = headA
        q = headB
        while p != q:

            if p is None:
                p = headB
            else:
                p = p.next

            if q is None:
                q = headA
            else:
                q = q.next
        return p
    