# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        ans = None
        head = None
        cnt = 0
        for lis in lists:
            cnt +=1
            while lis:
                heapq.heappush(heap, (lis.val, lis))
                lis = lis.next
        while heap:
            val, node = heapq.heappop(heap)
            if not head:
                head = node
                ans = node
                ans.next = None
            else:
                ans.next = node
                ans = ans.next
                ans.next = None
        return head
        