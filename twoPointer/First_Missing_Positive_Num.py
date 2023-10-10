def solve(nums):
    print (nums)
    for i in range(len(nums)):
        if nums[i] == float('inf'):
            continue
        else:
            index = nums[i]-1
            nums[i] = float('-inf')
            while index < len(nums) and index >= 0:
                temp = nums[index]-1
                nums[index] = float('inf')
                index = temp
    print (nums)
    for i in range(len(nums)):
        if nums[i] == float('-inf'):
            return (i+1)
    return len(nums)+1

nums = [3,4,-1,1]
ans = solve(nums)
print(ans)