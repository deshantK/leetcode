import heapq
from collections import Counter
def solve(s):
    dic = Counter(s)
    heap = []
    result = ""
    pre = None
    for char, count in dic.items():
        heapq.heappush(heap, [-count, char])
    while heap or pre:
        if not heap:
            return ""
        count, char = heapq.heappop(heap)
        result = result + char
        count = count + 1

        if pre:
            heapq.heappush(heap, pre)
            pre = None
        if count != 0:
            pre = [count, char]
    return result

s = "aab"
print (solve(s))