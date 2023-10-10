def find(nums, target):
    left = 0
    right = len(nums)-1
    cnt = 0
    while left < right:
        while left < right and nums[left] + nums[right] >= target:
            right -=1
        cnt += right-left
        left +=1
    return cnt

nums = [0,0,0,0,0,0]
lower = 0
upper = 0
nums.sort()
print(find(nums, upper+1)-find(nums, lower))
