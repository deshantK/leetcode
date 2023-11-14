def solve(nums):
    max_ = min(nums)
    sum_ = 0
    for elm in nums:
        if sum_ + elm <= 0:
            if max_ < sum_+elm:
                max_ = sum_+elm
            sum_ = 0
        else:
            sum_ +=elm
            if sum_ > max_:
                max_ = sum_
    return max_