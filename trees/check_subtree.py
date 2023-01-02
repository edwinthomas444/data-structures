'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false'''

'''VImp Note: 
Below doesnt work as first condition checks for exact match
and second condition recursive calls checks for if subtree matches or not
so both cant be combined to one recursive call (instead check exact must be another recursive method)
return (root.val == subRoot.val and (self.isSubtree(root.left,subRoot.left) 
and self.isSubtree(root.right,subRoot.right))) or (self.isSubtree(root.left,subRoot) 
or self.isSubtree(root.right,subRoot))'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check_exact(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        return (root.val == subRoot.val and (self.check_exact(root.left,subRoot.left) and self.check_exact(root.right,subRoot.right)))

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if not subRoot:
            return True
        if not root:
            return False
        
        if self.check_exact(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


