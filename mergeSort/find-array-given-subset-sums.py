import copy
def solve(nums, index, sum_, target, cnt, ans):
    if cnt == 0 and sum_ == target:
        return True
    if cnt == 0:
        return False
    if index == len(nums):
        return False

    ans.append(nums[index])
    check = solve(nums, index+1, sum_+nums[index], target, cnt-1, ans)
    if check:
        return check
    ans.pop(-1)
    check = solve(nums, index+1, sum_, target, cnt, ans)
    return check



n = 3
sums = [-3,-2,-1,0,0,1,2,3]
ans = []
target = sum(sums)//pow(2,n-1)
check = solve(sums, 0, 0, target, n, ans)
print (check, target, ans)