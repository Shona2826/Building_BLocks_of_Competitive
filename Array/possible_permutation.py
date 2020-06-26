class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        adj = collections.defaultdict(list)
        print(adj)
        for d in dislikes:
            adj[d[0]].append(d[1])
            adj[d[1]].append(d[0])  
        colors = {}
        queue  = collections.deque()
        for i in range(1,N+1):
            if i not in colors and adj[i]:
                colors[i] = 1
                queue.append((i))
                while(queue):
                    curr=queue.popleft()
                    for nb in adj[curr]:
                        if nb not in colors:
                            colors[nb] = 1 - colors[curr]
                            queue.append(nb)
                        elif colors[nb] == colors[curr]:
                            return False
        return True
                
        