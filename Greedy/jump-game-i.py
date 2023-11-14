def solve(nums):
    dp = [False]*len(nums)
    index = len(nums)-1
    dp[index] = True
    lastTrue = index
    index -=1
    while index >= 0:
        jump = nums[index]
        if index + jump >= lastTrue:
            dp[index] = True
            lastTrue = index
        index -=1

    return dp


nums = [3,2,1,0,4]
print (solve(nums))