'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr_l1 = list1
        ptr_l2 = list2

        # base conditions
        if not ptr_l1:
            return ptr_l2
        elif not ptr_l2:
            return ptr_l1
        

        head_ptr = ptr_l1 if ptr_l1.val<ptr_l2.val else ptr_l2

        while True:
            # choose a list based on minimum current value
            if ptr_l1.val>=ptr_l2.val:
                temp = ptr_l1
                ptr_l1 = ptr_l2
                ptr_l2 = temp

            # find point is list 1 where list 2 head can be inserted
            # after insertion, list 1 head becomes disjoint as found positions 
            # in list 1 next element
            prev_ptr = ptr_l1
            curr_ptr = ptr_l1.next
            while curr_ptr:
                if curr_ptr.val>=ptr_l2.val:
                    break
                else:
                    prev_ptr = curr_ptr
                    curr_ptr=curr_ptr.next
            

            # connect l1 found prev node to l2 current
            ptr_l1 = prev_ptr.next
            prev_ptr.next = ptr_l2
            
            # if any list head reaches None, it implies all are connected
            if not ptr_l2 or not ptr_l1:
                break
        
        return head_ptr
            
            
