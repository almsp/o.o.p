class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        visited = set()
        num_components = 0
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                num_components += 1
        
        num_cables_needed = num_components - 1
        
        if len(connections) < num_cables_needed:
            return -1
        
        return num_cables_needed