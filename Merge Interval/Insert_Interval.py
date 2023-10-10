def solve(intervals, newInterval):
    index = 0
    ans = []
    check = False
    while index < len(intervals):
        interval = intervals[index]
        
        if max(interval[0], newInterval[0]) <= min(interval[1], newInterval[1]):
            interval[0] = min(interval[0], newInterval[0])
            interval[1] = max(interval[1], newInterval[1])
            index +=1
            while index < len(intervals) and max(interval[0], intervals[index][0]) <= min(interval[1], intervals[index][1]):
                interval[0] = min(interval[0], intervals[index][0])
                interval[1] = max(interval[1], intervals[index][1])
                index +=1
            check = True
        elif newInterval[1] < interval[0] and not check:
            ans.append(newInterval)
            check = True
            index +=1
        else:
             index +=1
        ans.append(interval)

    if not check:
            ans.append(newInterval)
    return ans

        





intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [0,0]
ans = solve(intervals, newInterval)
print (ans)