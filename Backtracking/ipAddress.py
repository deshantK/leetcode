import copy
def is_valid(s):
    if len(s) > 1 and s[0]=='0':
        return False
    try:
        if 0 <= int(s) <= 255:
            return True
        return False
    except ValueError:
        return False


def solve(s, n, ipStr, result):
    if n == 4:
        if len(s) == 0:
            result.add(ipStr)
        return
    for i in range(1,4):
        str_ = s[0:i]
        check = is_valid(str_)
        if check:
            if n == 0:
                ipStr_ = copy.copy(str_)
            else:
                ipStr_ = copy.copy(ipStr)+"."+copy.copy(str_)
            solve(s[i:len(s)], n+1, ipStr_, result)
            

s = "201023"
result = set()
solve(s, 0, "", result)
print (list(result))