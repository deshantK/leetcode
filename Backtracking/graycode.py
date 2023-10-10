def con_int(str_):
    lis = list(str_)
    ans = 0
    index = 0
    while index < len(lis):
        ans += int(lis[index])*pow(2, index)
        index += 1
    return ans

def solve(code, dic, result, size_):
    if len(result) == size_:
        return
    index = 0
    while index < len(code):
        temp = code[index]
        if code[index] == "0":
            code[index] = "1"
        else:
            code[index] = "0"
        str_ = ''.join(code)
        if str_ not in dic:
            result.append(con_int(str_))
            dic[str_] = 0
            solve(code, dic, result, size_)
            return
        code[index] = temp
        index = index+1


n = 4
code = ["0"]*n
dic = {}
result = []
str_ = ''.join(code)
result.append(0)
dic[str_] = 0
size_ = pow(2,n)
solve(code, dic, result, size_)
print (result)