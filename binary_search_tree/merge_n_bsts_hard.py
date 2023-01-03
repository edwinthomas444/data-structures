'''
You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:

Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
Replace the leaf node in trees[i] with trees[j].
Remove trees[j] from trees.
Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.

A BST (binary search tree) is a binary tree where each node satisfies the following property:

Every node in the node's left subtree has a value strictly less than the node's value.
Every node in the node's right subtree has a value strictly greater than the node's value.
A leaf is a node that has no children.

Input: trees = [[2,1],[3,2,5],[5,4]]
Output: [3,2,5,1,null,4]
Explanation:
In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check_valid_BST(self, root, left_range, right_range):
        if not root:
            return True
        
        left_valid = self.check_valid_BST(root.left, left_range, root.val)
        right_valid = self.check_valid_BST(root.right, root.val, right_range)
        if root.val>left_range and root.val<right_range and left_valid and right_valid:
            return True
        else:
            return False


    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        # at any point the leaf nodes of k trees must be unique, otherwise, after merge, it doesnt satisfy stricly less and greater conditions
        # run the trees and store dict of leaf node value and tree index
        # if one leaf node value can map to more than 1 tree, means, after merge, the tree wont contain unique values and wont be a BST..
        # return -1
        # else merge them
        if len(trees) == 1:
            return trees[0]

        leaf2ind = {}
        for ind, tree in enumerate(trees):
            if tree.left:
                leaf2ind[tree.left.val] = (ind, 'L', tree)
            if tree.right:
                leaf2ind[tree.right.val] = (ind, 'R', tree)

        ind2leaf = {}
        for ind, tree in enumerate(trees):
            if tree.left:
                if ind in ind2leaf:
                    ind2leaf[ind].add(tree.left.val)
                else:
                    ind2leaf[ind] = set([tree.left.val])
            if tree.right:
                if ind in ind2leaf:
                    ind2leaf[ind].add(tree.right.val)
                else:
                    ind2leaf[ind] = set([tree.right.val])

        count_root = 0
        # store pointer to merged tree root
        pointer_merged = None
        for child_ind, tree in enumerate(trees):
            if count_root>1:
                # more than one tree that couldnt find a leaf node to any other sub-tree at any point-> cant merge
                return None

            # if only one node in tree
            if not tree.left and not tree.right:
                if tree.val not in leaf2ind:
                    return None
                else:
                    continue

            # check if roots value in leaf2ind
            if tree.val in leaf2ind:
                # merge trees
                parent_ind, path, parent_leaf_pointer = leaf2ind[tree.val]
                
                if parent_ind == child_ind:
                    return None

                if path == 'L':
                    parent_leaf_pointer.left = tree
                elif path == 'R':
                    parent_leaf_pointer.right = tree

                # update the leaf2ind to remove the leaf of the parent tree
                del leaf2ind[tree.val]
                # update the ind2leaf to remove the leaf of the child tree
                ind2leaf[parent_ind].remove(tree.val)


                # update new leaves of the parent tree
                # update the leaf2ind based on index of the parent tree
                child_leaves = ind2leaf[child_ind]
                for leaf in child_leaves:
                    ind2leaf[parent_ind].add(leaf)
                    # also update ind2leaf of child , basically remove it
                    # ind2leaf[child_ind].remove()
                    
                    # as all child leaves now belong to parent tree, its index needs to be udpated
                    if leaf not in leaf2ind:
                        return None
                    _, path, child_leaf_pointer = leaf2ind[leaf]
                    leaf2ind[leaf] = (parent_ind, path, child_leaf_pointer)

                # update root of merged tree to point to the parent
                pointer_merged = trees[parent_ind]
            else:
                pointer_merged = trees[child_ind]
                count_root+=1


        # check if merged bst is valid
        if count_root>1:
            return None

        check_bst = self.check_valid_BST(pointer_merged, 0, 5*10000+1)
        if check_bst:
            return pointer_merged

        return None             
                
                
