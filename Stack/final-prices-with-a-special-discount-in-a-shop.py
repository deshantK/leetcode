def finalPrices(prices):
    stack = []
    index = len(prices)-1
    ans = []
    while index >= 0:
        while stack and stack[-1] > prices[index]:
            stack.pop(-1)
        if not stack:
            ans.insert(0, prices[index])
        else:
            ans.insert(0, prices[index]-stack[-1])
        stack.append(prices[index])
        index -=1
    return ans

prices = [8,4,6,2,3]
ans = finalPrices (prices)
print (ans)