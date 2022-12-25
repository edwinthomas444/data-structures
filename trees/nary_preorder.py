'''Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]'''

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def compute_preorder(self, root, soln_list):
        if root:
            soln_list.append(root.val)
            for child in root.children:
                self.compute_preorder(child, soln_list)
        return soln_list
        
    def preorder(self, root):

        """
        :type root: Node
        :rtype: List[int]
        """
        return self.compute_preorder(root, [])