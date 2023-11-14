class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1  
        p2 = n - 1 
        x = 0
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            x += 1
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        return nums1


        
        