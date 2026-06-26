# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return res
        q.append((root,0))
        cur_level=0
        level_nodes=[]
        while len(q)>0:
            node, level = q.popleft()
            if level> cur_level:
                res.append(level_nodes)
                level_nodes = []
                cur_level+=1
            level_nodes.append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        res.append(level_nodes)
        return res
            