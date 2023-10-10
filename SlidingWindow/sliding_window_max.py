import heapq
def solve(nums, k):
    left = 0
    right = 0
    mheap = []
    ans = []
    while right < k:
        heapq.heappush(mheap,(-nums[right], right))
        right +=1
    ans.append(-mheap[0][0])
    while right < len(nums):
        left +=1
        while mheap[0][1] < left:
            heapq.heappop(mheap)
        heapq.heappush(mheap, (-nums[right], right))
        ans.append(-mheap[0][0])
        right +=1
    return ans

    
    





nums = [1,2,-1,-4,8,3,61,70, -1, -2, -3, 0]
k = 3
ans = solve(nums, k)
print(ans)