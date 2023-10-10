def dfs(node, edges, ans):
    graph = {}
    visited = set()
    for e in edges:
        u, v = e[0], e[1]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    stack = []
    stack.append(node)
    while stack:
        node_ = stack.pop()
        if node_ not in visited:
            visited.add(node_)
            ans.append(node_)
            edges_ = graph[node_]
            for e in edges_:
                stack.append(e)
    



A = 1
B = [ (1, 2), (4, 1), (2, 4),(3, 4), (5, 2), (1, 3)]
ans = []
dfs(A, B, ans)
print (ans)