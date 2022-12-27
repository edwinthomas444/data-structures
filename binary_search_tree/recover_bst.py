'''You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.'''


# IDEA:
# 1. consider traversal in inorder fashion recursively
# 2. maintain 3 ptrs to track changes in ascending order trend due to swaps
# 3. finally swap them

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, first, middle, last, prev_node):
        
        if not root:
            return

        self.inorder(root.left, first, middle, last, prev_node)
        if prev_node[0] and root.val < prev_node[0].val:
            if not first[0]:
                first[0] = prev_node[0]
                middle[0] = root
            else:
                last[0] = root

        prev_node[0] = root
        self.inorder(root.right, first, middle, last, prev_node)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = [None]
        middle = [None]
        last = [None]
        prev_node = [None]

        
        self.inorder(root, first, middle, last, prev_node)


        # swap them
        if last[0]:
            # all three are popoulated , not adjacent errors
            first[0].val, last[0].val = (last[0].val, first[0].val)
        else:
            # adjacent errors
            first[0].val, middle[0].val = (middle[0].val, first[0].val)

        