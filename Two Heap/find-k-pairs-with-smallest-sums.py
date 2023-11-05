import heapq
def solve(num1, num2, k):
    heap = []
    heapq.heappush(heap, (num1[0]+num2[0], 0, 0))
    ans =[]
    vis = set()
    vis.add((0,0))
    i = 0
    while i < k and heap:
        _sum, index1, index2 = heapq.heappop(heap)
        pair = [num1[index1], num2[index2]]
        ans.append(pair)
        if index1< len(num1)-1 and (index1+1, index2) not in vis:
            heapq.heappush(heap, (num1[index1+1]+num2[index2], index1+1, index2))
            vis.add((index1+1, index2))
        if index2 < len(num2)-1 and (index1, index2+1) not in vis:
            heapq.heappush(heap, (num1[index1]+num2[index2+1], index1, index2+1))
            vis.add((index1, index2+1))
        if index1 < len(num1)-1 and index2 < len(num2)-1 and (index1+1, index2+1) not in vis:
            heapq.heappush(heap, (num1[index1+1]+num2[index2+1], index1+1, index2+1))
            vis.add((index1+1, index2+1))
        i +=1
    return ans



nums1 = [1,1,2]
nums2 = [1,2,3]
k = 15
ans = solve(nums1, nums2, k)
print (ans)