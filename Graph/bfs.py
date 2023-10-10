import queue
def bfs(node, edges, ans):
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
    q = queue.Queue()
    q.put(node)
    print ("hi")
    while q.qsize() != 0:
        node_ = q.get()
        #print (node_)
        if node_ not in visited:
            visited.add(node_)
            ans.append(node_)
            edges_ = graph[node_]
            for e in edges_:
                q.put(e)
    


#print ("hi")
A = 1
B = [ (1, 2), (4, 1), (2, 4),(3, 4), (5, 2), (1, 3)]
ans = []
bfs(A, B, ans)
print (ans)