import heapq
from collections import defaultdict
#times =[[4, 2, 76], [1, 3, 79], [3, 1, 81], [4, 3, 30], [2, 1, 47], [1, 5, 61], [1, 4, 99], [3, 4, 68], [3, 5, 46], [4, 1, 6], [5, 4, 7], [5, 3, 44], [4, 5, 19], [2, 3, 13], [3, 2, 18], [1, 2, 0], [5, 1, 25], [2, 5, 58], [2, 4, 77], [5, 2, 74]]
times = [[1, 2, 5], [1, 3, 10], [1, 4, 15]]
n =4
k = 1
dic =  defaultdict(list)
for src, des, time in times:
    dic[src].append((time, des))
print (dic)
visited = set()
heap = []
delay = 0
heapq.heappush(heap, (0, k))
while heap:
    print (heap)
    time, node = heapq.heappop(heap)
    if node not in visited:
        visited.add(node)
        print (visited)
        neighbours = dic[node]
        delay = max(delay, time)
        for neighbour in neighbours:
            neighbour_time, neighbour_node = neighbour
            neighbour_time +=time
            heapq.heappush(heap, (neighbour_time, neighbour_node))
print (delay)
