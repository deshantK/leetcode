def solve(s, k):
    if k <= 1:
        return len(s)
    if len(s) < k:
        return 0
        
    freq = {}
    for i in range(len(s)):
        ch = s[i]
        if ch in dic:
            freq[ch] +=1
        else:
            freq[ch] = 1
    
    left


str_ = "aaabb"
k = 3
ans = solve(str_, k)
print(ans)