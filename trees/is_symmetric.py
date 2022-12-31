'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_symmetric(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1:
                return False
            elif not root2:
                return False

            # consider is_symmetric as checking whether the they are equal given by first condition
            return (root1.val ==  root2.val) and (is_symmetric(root1.left, root2.right) and is_symmetric(root1.right, root2.left))
        
        return is_symmetric(root.left, root.right)