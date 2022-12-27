'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # keeping track of min and max of each sub-tree
    def check_valid_soln2(self, root):
        if not root:
            return True, 2e+31, -2e31

        left_balanced, min_l, max_l = self.check_valid(root.left)
        right_balanced, min_r, max_r = self.check_valid(root.right)

        # validating left and right subtree w.r.t to root
        left_correct = not root.left or (root.left and root.val>max_l)
        right_correct =  not root.right or (root.right and root.val<min_r)


        if left_balanced and left_correct and right_balanced and right_correct:
            return True, min(root.val, min_l, min_r), max(root.val, max_l, max_r)
        else:
            return False, min(root.val, min_l, min_r), max(root.val, max_l, max_r)

    # passing ranges of min and max values as part of function
    # alternative way to implement but same idea
    def check_valid_soln1(self, root, min_val, max_val):
        if not root:
            return True
        
        left_valid = self.check_valid_soln1(root.left, min_val, root.val)
        right_valid = self.check_valid_soln1(root.right, root.val, max_val)
        root_valid = root.val>min_val and root.val<max_val

        # check validity with root
        if left_valid and right_valid and root_valid:
            return True
        else:
            return False


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        valid = self.check_valid_soln1(root, -2e+31, +2e+31)
        return valid