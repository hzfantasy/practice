# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        r = h
        while l1 and l2:
            if l1.val >= l2.val:
                r.next = l2
                l2 = l2.next
            else:
                r.next = l1
                l1 = l1.next
            r = r.next
        if l1:
            r.next = l1
        elif l2:
            r.next = l2
        return h.next
