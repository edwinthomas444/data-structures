# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_height(self, root):
        if not root:
            return 0
        return 1+max(self.find_height(root.left), self.find_height(root.right))

    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def level_order(root, height, arr):
            # find max height of left and right sub-trees min(max_left, max_right) = level for width
            if height == 0:
                if root and not arr[0]:
                    arr[0] = root
                elif root:
                    arr[1] = root
            else:
                if root:
                    level_order(root.left, height-1, arr)
                    level_order(root.right, height-1, arr)

        def find_index(root, node, level, range_left, range_right, found):
            if not root:
                return range_right

            if level>=1:
                find_index(root.left, node, level-1, range_left, range_right-2**(level-1), found)
                find_index(root.right, node, level-1, range_left+2**(level-1), range_right, found)
            if root == node:
                found[0] = range_right
                

        # main logic
        
        # 1. find height of tree to traverse through levels
        height_tree = self.find_height(root)
        # print(height_tree)

        # 2. for each level find left most and rigth most nodes if they exist
        ans = 0
        for width_level in range(0,height_tree):
            # print('level: ', width_level)
            # stores left most and right most node of a given level
            arr = [None, None]
            level_order(root, width_level, arr)
            left_node, right_node = arr
            # print(arr)

            # if both nodes exists, find their indexes at their level
            # ans would be max of difference between indices within all levels
            if left_node and right_node:
                first_elem_ind, second_elem_ind = [None], [None]
                find_index(root, left_node, width_level, 0, 2**width_level, first_elem_ind)
                find_index(root, right_node, width_level, 0, 2**width_level, second_elem_ind)
                # print(first_elem_ind, second_elem_ind)
                ans = max(ans, second_elem_ind[0]-first_elem_ind[0]+1)
            elif left_node:
                first_elem_ind = [None]
                find_index(root, left_node, width_level, 0, 2**width_level, first_elem_ind)
                ans = max(ans, 1)
                
        return ans
