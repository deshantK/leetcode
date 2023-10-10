def binary_search_rotated(nums, target):
  start = 0
  end = len(nums) -1
  while start <= end:
    mid = (start+end)//2
    num = nums[mid]
    if num == target:
      return mid
    elif target <= num:
      if target >= nums[start] and num > nums[start]:
        end = mid -1
      else:
        start = mid+1
    else:
      if target >= nums[end]:
        start = mid+1
      else:
        end = mid-1
    
  return -1

nums = [4,5,6,7,8,1,2,3]
target = 8
index = binary_search_rotated(nums, target)
print (index)