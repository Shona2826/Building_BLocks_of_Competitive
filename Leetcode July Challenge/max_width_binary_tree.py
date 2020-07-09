class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue = collections.deque([(root, 1)]) # root and the node number
        next_level = collections.deque([])
        res = 1
        while(queue):
            curr, node_num = queue.popleft()
            if curr.left:
                next_level.append((curr.left, node_num * 2))
            if curr.right:
                next_level.append((curr.right, node_num * 2 + 1))
            
            if len(queue) == 0 and next_level:
                res = max(next_level[-1][1] - next_level[0][1] + 1, res)
                queue, next_level = next_level, queue
        return res
        