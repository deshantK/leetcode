import heapq
def solve(A):
    start = []
    end = []
    for i in range(len(A)):
        heapq.heappush(start, A[i][0])
        heapq.heappush(end, A[i][1])
    cnt = 0
    ans = 0
    while start:
        while end[0] <= start[0]:
            heapq.heappop(end)
            cnt -=1
        heapq.heappop(start)
        cnt +=1
        ans = max(cnt, ans)
    return ans

        





A =  [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]]
ans = solve(A)
print(ans)