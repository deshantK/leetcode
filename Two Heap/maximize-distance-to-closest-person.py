import heapq
import math
def solve(seats):
    cnt = 0
    left = -1
    max_ = 0
    ans_index = -1
    right = 0
    while right < len(seats):
        check = seats[right]
        if check:
            if left == -1:
                max_ = cnt
            else:
                if ans_index == -1:
                    if 2*max_ < cnt:
                        ans_index = left
                        max_ = cnt
                else:
                    if max_ < cnt:
                        ans_index = left
                        max_ = cnt
            left = right
            cnt = 0     
        else:
            cnt +=1
        right +=1

    if ans_index == -1:
        return max(max_, cnt)
    else:
        return int(max(math.ceil(max_/2), cnt))
        

def solve2(seats):
    left = -1
    right = 0
    cnt = 0
    heap = []
    while right < len(seats):
        check = seats[right]
        if check:
            if left == -1:
                heapq.heappush(heap, -2*cnt)
            else:
                heapq.heappush(heap, -cnt)
            cnt = 0
            left = right
        else:
            cnt +=1
        right +=1
    heapq.heappush(heap, -2*cnt)
    return int(math.ceil(-heap[0]/2))

    

seats = [0,0,1]




print(solve(seats))
print(solve2(seats))