import heapq
def solve(a, b, c):
    heap = []
    heapq.heappush(heap, [-a, 'a'])
    heapq.heappush(heap, [-b, 'b'])
    heapq.heappush(heap, [-c, 'c'])
    pre = None
    result = ""
    while heap:
        if result and result[-1] == heap[0][1]:
            break
        count, char = heapq.heappop(heap)
        if abs(count) > 1:
            if pre and abs(abs(count)-abs(pre[1]) == 1):
                

            result = result + char
            count +=1
        elif abs(count) > 1:
            result = result + char + char
            count +=2
        if pre:
            heapq.heappush(heap, pre)
            pre = None
        if count != 0:
            pre = [count, char]
        print (result)
        print (heap)
    return result



a = 0
b = 8 
c = 11

print(solve(a, b, c))