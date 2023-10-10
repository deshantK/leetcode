from collections import Counter
def solve(s, w):
    freq = Counter(w)
    print(freq)
    k = len(w[0])
    ans = []
    size = k*len(words)
    for i in range(len(s)-size+1):
        right = i
        dic = {}
        while right < i+size:
            key = s[right:right+k]
            if key in freq:
                if key not in dic:
                    dic[key] = 1
                else:
                    dic[key] +=1
            else:
                break
            right +=k
        if dic == freq:
            ans.append(i)
    return ans



s = "barfoothefoobarman"
words = ["foo","bar"]
ans = solve(s, words)
print (ans)
