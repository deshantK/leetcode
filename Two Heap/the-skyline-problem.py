import heapq
def solve1(buildings):
    heap = []
    ans = []
    stream = []
    for build in buildings:
        stream.append([build[0], build[2], 's'])
        stream.append([build[1], build[2], 'e'])
    stream.sort(key = lambda x:x[0])
    dic = {}
    for s in stream:
        if s[2] == 's':
            if not ans:
                ans.append([s[0],s[1]])
            elif not heap:
                if ans[-1][0] == s[0]:
                    ans.pop()
                    if ans[0][1] < s[1]:
                        ans.append([s[0],s[1]])
                else:
                    ans.append([s[0], s[1]])                
            elif s[1] > -heap[0]:
                if ans[0][0] == s[0]:
                    ans[0][1] = s[1]
                else:
                    ans.append([s[0], s[1]])
            heapq.heappush(heap, -s[1])
        else:
            if s[1] == -heap[0]:
                heapq.heappop(heap)
                while heap and -heap[0] in dic:
                    key = -heapq.heappop(heap)
                    dic[key] -= 1
                    if dic[key] == 0:
                        del dic[key]
                if not heap:
                    ans.append([s[0],0])
                else:
                    ans.append([s[0], -heap[0]])
            else:
                if s[1] in dic:
                    dic[s[1]] +=1
                else:
                    dic[s[1]] = 1
    return ans


        








buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
ans = solve2(buildings)
print(ans)