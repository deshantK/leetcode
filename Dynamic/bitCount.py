n = 2
ans = [-1]*(n+1)
ans[0] = 0
for i in range(1,n+1):
    num = i
    ans[i] = num%2 + ans[num//2]
print(ans)