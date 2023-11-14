def countSubstrings(s):
    count = 0
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        count += 1
    for i in range(len(s)-1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        count += dp[i][i + 1]

    for length in range(3, len(s)+1):
        i = 0
        for j in range(length-1, len(s)):
            dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
            count += dp[i][j]
            i+=1
    return count

s = "aaa"
ans = countSubstrings(s)
print (ans)