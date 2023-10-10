def solve(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]  # Move one step
        fast = nums[nums[fast]]  # Move two steps
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow        
    

nums =[1,3,4,2,2]
ans = solve(nums)
print(ans)