def solve(coins, amount, dp):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if dp[amount] != float('inf'):
        return dp[amount]
    
    index = len(coins)-1
    min_ = float('inf')
    for s in coins:
        val = solve(coins, amount-s, dp)
        if val >= 0 and val < min_:
            min_ = val+1
            
    if min_ != float('inf'):
        dp[amount] = min_
    else:
        dp[amount] = -1
    return dp[amount]





coins = [186,419,83,408]
amount = 6249
dp = [float('inf')]*(amount+1)
coins.sort()
print(coins)
val = solve(coins, amount, dp)
print (val)