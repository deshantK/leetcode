def solve(nums, index, target, cur_sum, cur_res, ans, prev):
    if index == len(nums):
        if cur_sum ==  target:
            ans.append(cur_res)
        return
    for i in range(index, len(nums)):
        cur_str = nums[index:i+1]
        cur_num = int(cur_str)
        if not cur_res:
            solve(nums, i+1, target, cur_num, cur_str, ans, cur_num)
        else:
            solve(nums, i+1, target, cur_sum+cur_num, cur_res+"+"+cur_str, ans,cur_num)
            solve(nums, i+1, target, cur_sum-cur_num, cur_res+"-"+cur_str, ans,-cur_num)
            solve(nums, i+1, target, (cur_sum-prev)+(prev*cur_num), cur_res+"*"+cur_str, ans,cur_num*prev)
        if nums[index] == '0':
            break
    return
    



nums =  "105"
target = 5
ans = []
solve(nums, 0, target, 0, "", ans, 0)
print (ans)