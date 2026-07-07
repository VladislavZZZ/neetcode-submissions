# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def dfs(cur):
            if not cur:
                out.append("_")
                return
            out.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return ",".join(out)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.cur = 0
        def dfs():
            if nodes[self.cur] == "_":
                self.cur +=1
                return
            node = TreeNode(int(nodes[self.cur]))
            self.cur+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()