'''Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1. perform level order traversal using BFS - queues
        # 2. find left most and right most non null node in each level
        # 3. index during traversal is a global running variable starting from root as 1 and left, right as 2*i, 2*i+1
        # 4. find difference of index of each level and max of all levels is the desired answer

        queue = [(root, 1)]
        ans = 0
        # level order traversal
        # queue stores previous level elements
        while queue:
            _, left_ind = queue[0]
            _, right_ind = queue[-1]
            ans = max(ans, right_ind-left_ind+1)

            # innitialize queue for next level
            next_level_queue = []
            # queue here stores previous level elements
            while queue:
                elem, ind = queue.pop(0)
                if elem.left:
                    next_level_queue.append((elem.left, 2*ind))
                if elem.right:
                    next_level_queue.append((elem.right, 2*ind+1))
            # make current queue same as next level queue
            queue = next_level_queue

        return ans