from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Тест 1
graph = {0: {1, 2}, 1: {2}, 2: {0, 3}, 3: {3}}
assert bfs(graph, 2) == {0, 1, 2, 3}

# Тест 2
graph = {0: {1, 2}, 1: {0, 2}, 2: {0, 1, 3}, 3: {2}}
assert bfs(graph, 0) == {0, 1, 2, 3}

# Тест 3
graph = {0: {1, 2}, 1: {2}, 2: {0, 3}, 3: {1}}
assert bfs(graph, 2) == {0, 1, 2, 3}

# Тест 4
graph = {0: set(), 1: {2}, 2: {1}}
assert bfs(graph, 0) == {0}
