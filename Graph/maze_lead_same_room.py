def number_of_paths(corridors):
    adj = {}
    cycle = 0
    #visited
    for u, v in corridors:
        if u not in adj:
            adj[u] = set()
        if v not in adj:
            adj[v] = set()
        adj[u].add(v)
        adj[v].add(u)
        ans = adj[u].intersection(adj[v])
        print (u, adj[u], v, adj[v])
        print (ans)
        cycle = cycle
        
    return cycle

corridors = [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4], [1, 5]]
ans = number_of_paths(corridors)
print (ans)