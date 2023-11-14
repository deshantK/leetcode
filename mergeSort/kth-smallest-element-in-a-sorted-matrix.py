import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        while heap and k > 1:
            _, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[i]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
            k -=1
        if k == 1:
            return heap[0][0]
        return None
    