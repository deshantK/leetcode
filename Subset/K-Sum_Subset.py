import copy
def get(set_, lis, k, n, result):
    if n == len(lis):
        if sum(set_) == k:
            result.append(set_)
        return
    s1 = copy.copy(set_)
    s2 = copy.copy(set_)
    s2.append(lis[n])
    n = n+1
    get(s1, lis, k, n, result)
    get(s2, lis, k, n, result)
    return
lis = [1,2,3,4,5]
set_ = []
result = []
get(set_, lis, 5, 0, result)
print (result)  