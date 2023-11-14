def solve(nums, index, total, target,result, totalSum, dp):
    if total == target and index == len(nums):
        result +=1
        return result
    if index >= len(nums):
        return 0
    if dp[index][totalSum+total] != -1:
        return dp[index][totalSum+total]
    rem = sum(nums[index:len(nums)])
    if total-rem <= target <= total+rem:
        val1 = solve(nums, index+1, total+nums[index], target ,result, totalSum, dp)
        val2 = solve(nums, index+1, total-nums[index],target ,result, totalSum, dp)
        dp[index][totalSum+total] = (val1+val2)
    else:
        dp[index][totalSum+total] = 0
    return dp[index][totalSum+total]
    

nums = [40,19,30,48,8,50,13,31,29,38,35,31,40,47,7,16,31,33,45,6]
target = 49
dp = [[-1] * (2 * sum(nums) + 1) for _ in range(len(nums)+1)]

val = solve(nums, 0, 0, target,0, sum(nums),dp)
print (val)

