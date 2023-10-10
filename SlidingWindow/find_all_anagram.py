from collections import Counter
def solve(s, p):
    freq = Counter(p)
    left = 0
    right = 0
    ans = []
    dic = {}
    while right < len(s):
        ch = s[right]
        if ch not in freq:
            left = right +1
            dic = {}
        else:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] +=1
                while dic[ch] > freq[ch]:
                    print (s[left])
                    print (dic)
                    dic[s[left]] -=1
                    left +=1
        if freq == dic:
            ans.append(left)
            dic[s[left]] -=1
            left +=1
        right +=1
    return ans


        





s = "cbaebabacd" 
p = "abc"
ans = solve(s, p)
print (ans)