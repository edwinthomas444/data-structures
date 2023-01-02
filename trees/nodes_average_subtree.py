'''Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.

Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def find_sum_count(root, sum, count, ans):
            if not root:
                return 0, 0
            
            left_sum, left_count = find_sum_count(root.left, sum, count, ans)
            right_sum, right_count = find_sum_count(root.right, sum, count, ans)

            sum_root = root.val+left_sum+right_sum
            count_root = 1+left_count+right_count

            if int(sum_root/count_root)==root.val:
                ans[0]+=1
            
            return sum_root, count_root
        
        # find answer
        ans = [0]
        find_sum_count(root, 0, 0, ans)
        return ans[0]

