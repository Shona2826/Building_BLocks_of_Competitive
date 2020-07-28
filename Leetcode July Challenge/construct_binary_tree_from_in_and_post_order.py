# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        a = postorder[-1]
        root = TreeNode(a)
        index = inorder.index(a)
        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]
        postorder_left = postorder[:index]
        postorder_right = postorder[index:-1]
        root.left = self.buildTree(inorder_left,postorder_left)
        root.right = self.buildTree(inorder_right,postorder_right)
        return root
        