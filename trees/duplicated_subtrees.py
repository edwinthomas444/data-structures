'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        cache_dict = {} # node to node pre-order traversal
        result = []
        def dfs(root, path):
            if not root:
                return '#'
            
            # for inorder traversal opening and closing brackets to be included to considers cases like 0#0#0#0# of left and right subtrees can be
            # same but in preorder scenario, as the root followed by left and right are printed in order, the tree can be uniquely reconstructed
            # so ( and ) can be excluded..

            # inorder traveral
            # path = path + '('+','.join([dfs(root.left,path), str(root.val), dfs(root.right, path)])+')'
            
            # preorder traversal
            path = path + ','.join([str(root.val), dfs(root.left,path), dfs(root.right, path)])
            # print('path',path)

            if path in cache_dict:
                cache_dict[path]+=1
                if cache_dict[path] == 2:
                    result.append(root)
            else:
                cache_dict[path] = 1

            return path

        dfs(root, '')
        return result
            
        