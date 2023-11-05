import copy
def solve(nums):
    result = []
    result.append([])
    if len(nums) == 0:
        return result
    result.append([nums[0]])
    if len(nums) == 1:
        return result
    index = 1
    pre_Index = 1
    while index < len(nums):
        counter = 0
        if nums[index] == nums[index-1]:
            counter = pre_Index
        n = len(result)
        pre_Index = n
        while counter < n:
            ls = copy.deepcopy(result[counter])
            ls.append(nums[index])
            result.append(ls)
            counter +=1
        index +=1
    return result



nums = [1,1,2,2]
ans = solve(nums)
print(ans)
