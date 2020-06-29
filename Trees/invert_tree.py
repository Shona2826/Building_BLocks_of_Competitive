class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        else:
            
            self.invertTree(root.left)
            #print(root)
            self.invertTree(root.right)
            
            root.left, root.right = root.right, root.left
            # print(root)
        
        return root