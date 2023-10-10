def solve(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    index1 = 0
    index2 = 0
    ans_len = float('inf')
    ans_str = ""
    while index1 < n1:
        if str1[index1] == str2[index2]:
            index2 +=1
            if index2 == n2:
                end = index1
                index2 -=1
                while index2 >= 0:
                    if str1[index1] == str2[index2]:
                        index2 -=1
                    index1 -=1
                
                index1 +=1
                start = index1
                if end - start < ans_len:
                    ans_len = end-start
                    ans_str = str1[start:end+1]
                index2 = 0
        index1 +=1


    return ans_str




str1 = "michmznaitnjdnjkdsnmichmznait"
str2 = "michmznait"
ans = solve(str1, str2)
print (ans)

