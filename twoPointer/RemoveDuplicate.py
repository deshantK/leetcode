def solve(nums):
    left = 0
    right = 1
    cnt = 1
    while right < len(nums):
        print (nums)
        print (left, right)
        if nums[left] == nums[right]:
            cnt +=1
            if cnt <= 2:
                left +=1
                if left < right:
                    nums[left] = nums[right]
            right +=1
        else:
            left +=1
            nums[left] = nums[right]
            right +=1
            cnt = 1
    return nums

nums = [0,0,1,1,1,1,2,3,3]
ans = solve(nums)
print(ans)