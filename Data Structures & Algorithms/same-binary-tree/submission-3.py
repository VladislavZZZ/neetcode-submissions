# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_equal(node1, node2):
            if not node1:
                return not node2
            if node2:
                right_is_same, left_is_same = is_equal(node1.right, node2.right), is_equal(node1.left, node2.left)
                return right_is_same and left_is_same and node2.val == node1.val
            else:
                return False
        
        return is_equal(p, q)