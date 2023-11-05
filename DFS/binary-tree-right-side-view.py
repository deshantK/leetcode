def solve(root, cur_ht, r_ht, ans):
    #print(cur_ht, r_ht)
    if not root:
        return r_ht
    if cur_ht == r_ht:
        ans.append(root.val)
        r_ht +=1
    r_ht = max (r_ht, solve(root.right, cur_ht+1, r_ht, ans))
    r_ht = max(r_ht, solve(root.left, cur_ht+1, r_ht, ans))
    return r_ht