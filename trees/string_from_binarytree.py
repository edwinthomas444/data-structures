'''Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root, path):
            if not root:
                return ''
            
            left_str = preorder(root.left, path)
            right_str = preorder(root.right, path)

            # below conditions to avoid bracketing null values whenever they can be ommited and tree still recovered
            if left_str and right_str:
                left_str = '(' + left_str + ')'
                right_str = '(' + right_str + ')'
            elif left_str:
                left_str = '(' + left_str + ')'
            elif right_str:
                left_str = left_str = '(' + left_str + ')'
                right_str = '(' + right_str + ')'

            path = path + ''.join([str(root.val) + left_str + right_str])
            return path
        
        path_str = preorder(root, '')
        return path_str
