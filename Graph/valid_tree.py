def valid_tree(n, edges):
    if len(edges) != n-1:
        return False
    adj = {}
    print ("n = ", n)
    for e in edges:
        u, v = e[0], e[1]
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
    #print (adj)
    stack = []
    visited = set()
    stack.append(edges[0][0])
    #print (stack[0])
    while stack:
        node = stack.pop()
        #print (node)
        if node in visited:
            #print ("Hi")
            return False
        visited.add(node)
        neighbors = adj[node]
        for n_ in neighbors:
            stack.append(n_)
    print (len(visited), n)
    if len(visited) == n:
        return True
    #print ("fff")
    return False

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [3, 4]]
check = valid_tree(n, edges)
print (check)