def solve(nums, n, total, dp):
    if total == 0:
        return True
    if total < 0 or n == len(nums):
        return False
    if dp[n][total] != -1:
        return dp[n][total]
    if nums[n] <= total:
        dp[n][total] = (solve(nums, n+1, total - nums[n], dp) 
                        or solve(nums, n+1, total,dp))
        return dp[n][total]
    dp[n][total] = solve(nums, n+1, total,dp)
    return dp[n][total]
    

nums = [1,5,11,5]
sum_ = sum(nums)
if sum_%2 != 0:
    print ("False")
else:
    total = sum_//2
    dp = [[-1 for i in range(total+1)] for j in range(len(nums))]
    check = solve(nums, 0, total, dp)
    print (check)