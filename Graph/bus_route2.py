def solve(route, adj, bus, src, dest):
    visited = set()
    stack = []
    stack.append((bus, 1))
    ans = float('inf')
    while stack:
        cur_bus, cnt = stack.pop(0)
        if cur_bus not in visited:
            visited.add(cur_bus)
            if dest in set(route[cur_bus]):
                ans = min(ans, cnt)
            connecting_bus = adj[cur_bus]
            for c_bus in connecting_bus:
                if c_bus not in visited:
                    stack.append((c_bus, cnt+1))
    return ans

    





route = [[10,13,22,28,32,35,43],[2,11,15,25,27],[6,13,18,25,42],[5,6,20,27,37,47],[7,11,19,23,35],[7,11,17,25,31,43,46,48],[1,4,10,16,25,26,46],[7,11],[3,9,19,20,21,24,32,45,46,49],[11,41]]
src = 37
dest = 43
adj = {}
n = len(route)
for i in range(n):
    if i not in adj:
        adj[i] = [i]
    for j in range(i+1, n):
        first = set(route[i])
        second = set(route[j])
        temp = first.intersection(second)
        if len(temp) > 0:
            if j not in adj:
                adj[j] = [j]
            adj[i].append(j)
            adj[j].append(i)

src_bus = []
for i in range(len(route)):
    if src in set(route[i]):
        src_bus.append(i)

#print (src_bus)
ans = float('inf')
for bus in src_bus:
    temp = solve(route, adj, bus, src, dest)
    if temp != float('inf'):
        ans = min(ans, temp)
if ans == float('inf'):
    print ("-1")
else:
    print (ans)