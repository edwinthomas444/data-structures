# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
1. find loop using slow and fast ptrs
2. then move both pointers one step at a time till they meet to find the start of the loop
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                break
        if slow_ptr != fast_ptr:
            return None
        else:
            # loop found
            # init slow_ptr as head and move both ptrs one at a time
            # to find beginning of loop
            slow_ptr = head
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            return slow_ptr
        