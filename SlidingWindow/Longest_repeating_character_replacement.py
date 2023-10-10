def solve(s, k):
    n = len(s)
    start = 0
    end = 0
    ans_len = 0
    max_char_freq = 0
    dic = {}
    while end < n:
        char_ = s[end]
        if char_ in dic:
            val = dic[char_]
            val = val+1
            dic[char_] = val
        else:
            dic[char_] = 1
        max_char_freq = max(dic[char_], max_char_freq)
        
        if (end-start-max_char_freq) > k:
            char_ = s[start]
            start = start+1
            val = dic[char_]
            dic[char_] = val-1

        ans_len = max(ans_len, end-start+1)
        end = end+1
    return ans_len







str_ = "aaaa"
k = 0
ans = solve(str_, k)
print(ans)