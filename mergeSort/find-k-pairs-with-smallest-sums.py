import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        ans = []
        i1 = 0
        i2 = 0
        heap = []
        heapq.heappush(heap, (nums1[i1]+nums2[i2], i1, i2))
        vis = set()
        vis.add((i1, i2))
        while heap and k > 0:
            
            _, index1, index2 = heapq.heappop(heap)
            print (index1, index2)
            ans.append([nums1[index1], nums2[index2]])
            if index1 + 1 < len(nums1) and (index1+1, index2) not in vis:
                heapq.heappush(heap, (nums1[index1+1]+nums2[index2], index1+1, index2))
                vis.add((index1+1, index2))
            if index2 + 1 < len(nums2) and (index1, index2+1) not in vis:
                heapq.heappush(heap, (nums1[index1]+nums2[index2+1], index1, index2+1))
                vis.add((index1, index2+1))
            k -=1
#            print (heap)
        
        return ans



        