from collections import Counter
def solve(s1, s2):
    dic = Counter(s1)
    left = right = 0
    ans = {}
    cnt = 0
    target = len(dic)
    while right < len(s2):
        str_ = s2[right]
            #print (str_, ans)
        if s2[right] not in dic:
            cnt = 0
            left = right+1
            ans = {}
        else:
            if str_ not in ans:
                ans[str_] = 1
            else:
                ans[str_] +=1
            if ans[str_] == dic[str_]:
                cnt +=1
            elif ans[str_] > dic[str_]:
                while ans[str_] > dic[str_]:
                    if ans[s2[left]] == dic[s2[left]]:
                        cnt -=1
                    ans[s2[left]] -=1
                    left = left+1
            if cnt == len(dic):
                #print (ans, cnt)
                return True
        right = right+1
    return False 

s1 = "ab"
s2 = "eidbaooo"
ans = solve(s1, s2)