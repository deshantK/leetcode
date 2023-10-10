def solve(nums):
    right = 0
    open = False
    ans = []
    while right < len(nums):
        p1 = nums[right]
        p2 = nums[right+1]
        if abs(p1-p2) == 1:
            right = right+2
            continue
        else:
            ans.append([p1, p2])
        right = right+2
    
    return ans

nums = [5,4,2,6,3,1,0,7]
ans = solve(nums)
print(ans)