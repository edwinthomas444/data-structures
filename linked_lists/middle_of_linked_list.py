'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3. '''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base conditions
        if not head or not head.next:
            return head
        
        ptr_one_step = head
        ptr_two_step = head
        while ptr_two_step is not None and ptr_two_step.next is not None:
            ptr_one_step = ptr_one_step.next
            ptr_two_step = ptr_two_step.next.next

            
        return ptr_one_step
