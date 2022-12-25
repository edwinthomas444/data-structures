'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # distance and the nodes belonging to it
        level_order = {} 


        queue  = []
        # node and distance from root
        queue.append((root,0))
        while queue:
            elem, dist = queue.pop(0)
            if elem:
                if dist in level_order:
                    level_order[dist].append(elem.val)
                else:
                    level_order[dist] = [elem.val]
                queue.append((elem.left, dist+1))
                queue.append((elem.right, dist+1))
        
        level_order = [level_order[dist] for dist in level_order]
        # print(level_order)
        return level_order


        
