def solve(coins, amount, dp):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if dp[amount] != float('inf'):
        return dp[amount]
    
    index = len(coins)-1
    min_ = float('inf')
    while index >= 0:
        s = coins[index]
        val = solve(coins, amount-s, dp)
        if val >= 0 and val < min_:
            min_ = val+1
        index -=1
    if min_ != float('inf'):
        dp[amount] = min_
    return dp[amount]





coins = [1,2,5]
amount = 11
dp = [float('inf')]*(amount+1)
val = solve(coins, amount, dp)
print (val)