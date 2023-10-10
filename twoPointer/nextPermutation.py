def reverse(A):
    left = 0
    right = len(A) -1
    while left < right:
        temp = A[left]
        A[left] = A[right]
        A[right] = temp
        left +=1
        right -=1
    return A

def nextPermutation( nums):
    right = len(nums)-1
    left = right - 1
    while left >= 0:
        if nums[left] < nums[right]:
            break
        left -=1
        right -=1
    if left < 0:
        print ("Hi")
        return reverse(nums)
    right = right+1
    while right < len(nums) and nums[left] < nums[right]:
        right +=1
    temp = nums[left]
    if right >= len(nums):
        right = len(nums)-1
    nums[left] = nums[right]
    nums[right] = temp
    left +=1
    right = len(nums)-1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left +=1
        right -=1
    return nums
        
nums = [2, 3, 1]
ans = nextPermutation(nums)
print(ans)