import heapq
def solve(messages, senders):
    dic = {}
    heap = []
    ans = []
    for i in range(len(senders)):
        key = senders[i]
        str_ = messages[i]
        st_lis = str_.split(" ")
        if key not in dic:
            dic[key] = len(st_lis)
        else:
            dic[key] +=len(st_lis)
    for key, val in dic.items():
        heapq.heappush(heap, [-val, key])
    
    max_ = heap[0][0]

    while heap and heap[0][0] == max_:
        ans.append(heapq.heappop(heap)[1])
    print (ans)
    return max(ans)
    


messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]
solve(messages, senders)