def solve(tasks, k):
    ans = 0
    dic = {}
    for t in tasks:
        if t in dic:
            dic[t] +=1
        else:
            dic[t] = 1
    dic = sorted(dic.items(), key=lambda x:x[1])
    max_= dic[-1][1]
    idle_time = (max_-1)*k
    index = len(dic)-2
    while index >= 0:
        idle_time -= min(max_-1, dic[index][1])
        index -=1
    idle_time = max(0, idle_time)
    ans = len(tasks)+idle_time
    return ans




tasks = ["A","A","A","B","B","B"]
n = 2