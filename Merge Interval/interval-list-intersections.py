def solve(lst1, lst2):
    ans = []
    index1 = 0
    index2 = 0
    while index1 < len(lst1) and index2 < len(lst2):
        if max(lst1[index1][0], lst2[index2][0]) <= min(lst1[index1][1], lst2[index2][1]):
            s1 = max(lst1[index1][0], lst2[index2][0])
            s2 = min(lst1[index1][1], lst2[index2][1])
            ans.append([s1, s2])
        if lst1[index1][1] > lst2[index2][1]:
            index2 +=1
        else:
            index1 +=1

    return ans




firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = []
ans = solve(firstList, secondList)
print(ans)