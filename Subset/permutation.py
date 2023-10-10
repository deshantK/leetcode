import copy

def swap(word, i, j):
    w_list = list(word)
    w_list[i], w_list[j] = w_list[j], w_list[i]
    return ''.join(w_list)

def get(word, current_index,result):
    print (current_index)
    if current_index == len(word):
        result.append(word)
        return
    
    for index in range(current_index, len(word)):
        str_ = swap(word, current_index, index)
        get(str_, current_index+1, result)

def fun():
    str__ = "abc"
    result = []
    get(str__, 0, result)
    print (result)
    
fun()
