def solve(tasks, space):
    dic = {}
    for t in tasks:
        if t not in dic:
            dic[t] = -1
    i = 0
    cnt = 0
    while i < len(tasks):
        cnt +=1        
        job = tasks[i]
        if dic[job] >= 0 and cnt - dic[job]-1 < space:
            pass_ = cnt-dic[job]-1
            cnt +=space-pass_
        i +=1
        dic[job] = cnt
    return cnt


tasks = [5,8,8,5]
space = 2
print (solve(tasks, space))