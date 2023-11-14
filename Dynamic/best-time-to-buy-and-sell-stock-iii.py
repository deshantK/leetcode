def solvedp(p, buy,index, cnt, dp):
    if cnt == 0:
        return 0
    if index == len(p):
        return 0
    if dp[buy][index][cnt] != -1:
        return dp[buy][index][cnt]
    if p[index] <= p[buy]:
        dp[buy][index][cnt] =  solvedp(p, index, index+1, cnt, dp)
    elif p[index] > p[buy]:
        val1 = solvedp(p, buy, index+1, cnt, dp)
        val2 = p[index]-p[buy] + solvedp(p, index, index+1, cnt-1, dp)
        dp[buy][index][cnt] =  max(val1, val2)
    return dp[buy][index][cnt]

def solve(p, buy,index, cnt):
    if cnt == 0:
        return 0
    if index == len(p):
        return 0
    if p[index] <= p[buy]:
        return solve(p, index, index+1, cnt)
    elif p[index] > p[buy]:
        val1 = solve(p, buy, index+1, cnt)
        val2 = p[index]-p[buy] + solve(p, index, index+1, cnt-1)
        return max(val1, val2)

p = [3,3,5,0,0,3,1,4]
dp = [[[-1, -1, -1] for _ in range(len(p)+1)] for _ in range(len(p)+1) ]

print (solvedp(p, 0, 0 ,2, dp))
#print (dp)
print (solve(p, 0, 0 ,2))
