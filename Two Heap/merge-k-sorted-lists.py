import heapq
def solve(nums, k):
    dic = {}
    for elm in nums:
        if elm in dic:
            dic[elm] +=1
        else:
            dic[elm] = 1
    heap = []
    for key in dic.keys():
        heapq.heappush(heap, (-dic[key], key))
    ans = []
    for i in range(k):
        val, key = heapq.heappop(heap)
        ans.append(key)
    return ans


nums = [1,1,1,2,2,3]
k = 2
ans = solve(nums, k)
print (ans)