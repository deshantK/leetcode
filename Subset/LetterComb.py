
def get(lis, result):
    n = len(result)
    ans = []
    print(lis)
    for l in lis:
        for i in range(n):
            str_ = str(l)+str(result[i])
            ans.append(str_)
    return ans




dic = {"1": '', "2": 'abc', "3": 'def', "4": 'ghi', "5":'jkl', "6": 'mno', "7":'pqrs', "8": 'tuv', "9":'wxyz'}
num = "29"
result = []
result.append("")
num_lis = list(num)
index = len(num_lis)-1
while index >= 0:
    result = get(list(dic[num_lis[index]]), result)
    index = index-1
print (result)
