'''Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inspired from max path sum pbm

# another approach to solve same is taking diameter as max(lheight+1+rheight, max(ldiameter, rdiameter)),
# i.d max of left and right diameters and the max of the one that includes the root...
# need to call another utility height function for finding height or find height during the recursive process..
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_edge_sum(root, with_split, without_split):
            if not root:
                return 0, without_split
            
            max_left, wo_l= max_edge_sum(root.left, with_split, without_split)
            max_right, wo_r = max_edge_sum(root.right, with_split, without_split)

            with_split = max(max_left, max_right) + 1 # 1 for root
            without_split = max(without_split, wo_l, wo_r, max_left+1+max_right)

            return with_split, without_split


        a,b = max_edge_sum(root,0,0)
        return b-1 # as node count is taken in previous case
