import heapq
def kthSmallest(matrix, k):
    heap = []
    for i in range(len(matrix)):
        heapq.heappush(heap, (matrix[i][0], i, 0))
    print (heap)
    while heap and k > 1:
        _, i, j = heapq.heappop(heap)
        if j+1 < len(matrix[i]):
            heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        k -=1
    if k == 1:
        return heap[0][0]
    return None





matrix = [[1,5,9],[10,11,13],[12,13,15]] 
k = 8
print (kthSmallest(matrix, k))