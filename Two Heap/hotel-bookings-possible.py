import heapq
def solve(a, d, c):
    heap = []
    cnt = 2
    for i in range(len(a)):
        while heap and heap[0] <= a[i]:
            cnt -=1
            if cnt < 0:
                return 0
            heapq.heappop(heap)
        heapq.heappush(heap, d[i])
        cnt +=1
        if cnt > c:
            return 0
    return 1




A = [1, 2, 3]
B = [2, 3, 4]
C = 2
ans = solve(A, B, C)
print(ans)