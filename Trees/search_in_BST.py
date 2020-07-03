class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return 
        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        elif val < root.val:
            return self.searchBST(root.left,val)
        