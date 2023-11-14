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

def solve(nums, index, dp, target):
    if target == 0:
        return 1
    if index == len(nums):
        return 0
    if dp[index][target] > 0:
        return dp[index][target]

    if target >= nums[index]:
        dp[index][target] = solve(nums, index+1, dp, target-nums[index]) + solve(nums, index+1, dp, target)
    else:
        dp[index][target] = solve(nums, index+1, dp, target)
    return dp[index][target]
    


lis = [4,3,2,3,5,2,1]
set_ = []
result = []
target = 5
get(set_, lis, target, 0, result)
print (result)  
dp = [[0 for i in range(target+1)] for j in range(len(lis)+1)]
print (solve(lis, 0, dp, target))
