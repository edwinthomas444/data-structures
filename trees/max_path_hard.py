'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_max_path(root, max_nosplit):
            if not root:
                return 0, max_nosplit

            # return value for left tree is max with split
            max_left_split, max_nosplit_l = find_max_path(root.left, max_nosplit)
            # return value of right subtree is max with split
            max_right_split, max_nosplit_r = find_max_path(root.right, max_nosplit)
            max_left_split = max(0, max_left_split)
            max_right_split = max(0, max_right_split)

            # max nosplit considers global max of including path through a traversed root and max of 
            # its left and right ones, the cases where a path through current node wont be included
            # is handled when we take max of this max_nosplit's previous value and current ones.
            # max_split is used to pass to the node above, where only one of the left or right maxs can be
            # used to form a path where the node doesnt repeat.. this is used in max nosplit variable
            # the path where only left or right path is maximum is considered when max_left_split = max(0,max_left_split)
            # i.e a max sum path wont include left branch or right branch if that branch is negative or adding it
            # reduces the sum, thats why 0 added in max expression to cut this path (hence all possibilities considered)
            
            max_nosplit = max(max_nosplit, max_nosplit_l, max_nosplit_r, max_left_split+root.val+max_right_split)
            max_split = max(max_left_split, max_right_split) + root.val
            return max_split, max_nosplit

        
        # call utility
        a,b = find_max_path(root, root.val)
        return b
        

            







