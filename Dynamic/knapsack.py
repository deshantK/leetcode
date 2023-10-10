def solve1(w, v, c, n, dp):
    if n == 0 or c < 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]
    if w[n-1] <= c:
        dp[n][c] = max(solve1(w, v, c, n-1, dp),
                       v[n-1]+solve1(w, v, c-w[n-1], n-1, dp))
        return dp[n][c]
    dp[n][c] = solve1(w, v, c, n-1, dp)
    return dp[n][c]

def solve2(w, v, c, n, dp):
    if n == len(w) or c <= 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]
    if w[n] <= c:
        dp[n][c] = max(solve2(w, v, c, n+1, dp),
                       v[n]+solve2(w, v, c-w[n], n+1, dp))
        return dp[n][c]
    dp[n][c] = solve2(w, v, c, n+1, dp)
    return dp[n][c]



weight = [10,20,30]
value = [22,33,44]
capacity = 30
dp1 =[[-1 for i in range(capacity+1)] for j in range(len(weight)+1)]
dp2 =[[-1 for i in range(capacity+1)] for j in range(len(weight)+1)]
val1 = solve1(weight, value, capacity, len(weight), dp1)
val2 = solve2(weight, value, capacity, 0, dp2)
print (val1)
print (val2)