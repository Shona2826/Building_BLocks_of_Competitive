class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = [False for i in range(len(graph))]
        res = []
        def dfs(node,ans):
            visited[node] = True
            if node == len(graph)-1:
                res.append(ans[:])
                return 
            for child in graph[node]:
                ans.append(child)
                dfs(child,ans)
                ans.pop()
        dfs(0,[0])
        return res