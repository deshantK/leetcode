def solve(nums, index, ans):
    right = len(nums)-1
    sq = 2*nums[index]
    while right > index:
        if nums[right] >= sq:
            ans.add(index)
            ans.add(right)
            break
        right -=1
    return

def maxNumOfMarkedIndices(nums):
    nums.sort()
    print (nums)
    ans = set()
    left = 0
    right = len(nums)-1
    for i in range(len(nums)):
        if i not in ans:
            solve(nums, i, ans)
    return ans

nums = [9,2,5,4]
ans = maxNumOfMarkedIndices(nums)
print (ans)