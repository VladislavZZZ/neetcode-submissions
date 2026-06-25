# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def get_subroot(root, subroot):
            res = []
            st = [root]
            while st:
                node = st[-1]
                st.pop()
                if node.val == subroot.val:
                    res.append( node)
                if node.left:
                    st.append(node.left) 
                if node.right:
                    st.append(node.right)
            return res
        subroot_nodes = get_subroot(root, subRoot)
        if len(subroot_nodes) == 0:
            return False
        def is_equal(node1, node2):
            if not node1:
                return not node2
            if node2:
                right_is_same, left_is_same = is_equal(node1.right, node2.right), is_equal(node1.left, node2.left)
                return right_is_same and left_is_same and node2.val == node1.val
            else:
                return False
        return True if True in [is_equal(subroot_node, subRoot) for subroot_node in subroot_nodes] else False
