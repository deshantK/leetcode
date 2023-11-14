def jump(self, nums):
    if len(nums)==1:
        return 0
    cnt = 1
    next_ = nums[0]
    index = 1
    n = len(nums)
    while index < n:
        max_ = next_
        while index <= next_ and index < n:
            temp = index + nums[index]
            if temp > max_:
                max_= temp
            if index == n-1:
                return cnt
            index+=1
        cnt +=1
        next_ = max_
    return cnt
    

nums = [2,3,1,1,4]
print (jump(nums))