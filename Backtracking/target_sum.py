def solve(nums, str_, index, total, target,result):
    if total == target and index == len(nums):
        result.append(str_)
        return
    if index >= len(nums):
        return
    rem = sum(nums[index:len(nums)])
    if total-rem <= target <= total+rem:
        nstr = str_+"+"+str(nums[index])
        solve(nums, nstr, index+1, total+nums[index], target ,result)
        nstr = str_+"-"+str(nums[index])
        solve(nums, nstr, index+1, total-nums[index],target ,result)
    else:
        return


nums =[25,18,47,13,45,29,15,45,33,19,39,15,39,45,17,21,29,43,50,10]
target =25
result = []
total = 0
solve(nums, "", 0, total ,target, result)
print (len(result))