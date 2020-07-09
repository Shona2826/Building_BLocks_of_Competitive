class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = []
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                head = q.pop(0)
                level.append(head.val)
                if head.left is not None:
                    q.append(head.left)
                if head.right is not None:
                    q.append(head.right)
            res.insert(0,level)
            
        return res
        