def solve(nums):
    dp = [0]*(len(nums)+1)
    dp[0] = 0
    dp[1] = nums[0]
    for i in range(2,len(dp)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
    return dp[-1]
def rob( nums):
    if len(nums) == 0 or nums is None:
        return 0
    if len(nums) <= 2:
        return max(nums)
    return max(solve(nums[:-1]), solve(nums[1:]))

nums = [2,3,2]
print (rob(nums))