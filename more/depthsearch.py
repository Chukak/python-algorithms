""" Depth search """


GRAPH = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['D', 'E', 'F'],
    'D': ['C', 'E'],
    'E': ['C', 'A', 'Y'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
}


def dfs(node, visited):
    if node not in visited:
        visited.add(node)
        for node_2 in GRAPH.get(node, []):
            dfs(node_2, visited)
    return sorted(visited)


def dfs_2(graph, node):
    visited, stack = set(), []
    v = node
    while v:
        if v not in visited:
            visited.add(v)
            stack.extend(set(graph.get(v, [])) ^ visited)
        v = stack.pop() if stack else None
    return sorted(visited)


print(dfs('A', set()))
print(dfs_2(GRAPH, 'A'))

