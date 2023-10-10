def check(w1, w2):
    if min(len(w1), len(w2))+1 != max(len(w1), len(w2)):
        return False
    index1 = 0
    index2 = 0
    cnt = 0
    while index1 < len(w1) and index2 < len(w2):
        if w1[index1] != w2[index2]:
            cnt +=1
            if cnt == 2:
                return False
            if len(w1) > len(w2)

            
            

def solve(words, index):

    return 




words = ["a","b","ba","bca","bda","bdca"]
ans = solve(words, 0)