import copy
def solve(nums, index, csum, target, vis, cnt):
    if cnt == 0:
        return True
    if csum == target:
        cnt -=1
        return solve(nums, 0, 0, target, vis, cnt)
        
    for i in range(index, len(nums)):
        elm = nums[i]
        if not vis[i] and csum + elm <= target:
            vis[i] = True
            check =  solve(nums, i+1, csum+elm, target, vis, cnt)
            if check:
                return True
            vis[i] = False
    return False

nums = [10,5,5,4,3,6,6,7,6,8,6,3,4,5,3,7]
k = 8

if sum(nums)%k != 0:
    print (False)

target = sum(nums)/k
rcnt = 0
vis = [False]*(len(nums))
check = solve(nums, 0, 0, target, vis, k)
print (check)

