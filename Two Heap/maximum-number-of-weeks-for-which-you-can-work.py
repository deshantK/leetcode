import heapq
def solve( milestones):
    heap = []
    for i in range(len(milestones)):
        heapq.heappush(heap, -milestones[i])
    cnt =0
    idle_time = -heapq.heappop(heap)-1
    while heap:
        job = heapq.heappop(heap)
        if idle_time >= abs(job):
            cnt -=2*job
            idle_time += job
        else:
            cnt = sum(milestones)
            return cnt
    if idle_time > 0:
        cnt +=1

    return cnt
nums = [3,2,1]
print (solve(nums))