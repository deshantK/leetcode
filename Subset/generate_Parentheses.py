def get(str_,n ,op_brc, cl_brc ,result):
    if op_brc > n or cl_brc > n:
        return
    if op_brc == cl_brc == n:
        result.append(str_)
        return
    if op_brc < cl_brc:
        return
    if op_brc == cl_brc:
        get(str_+'(', n, op_brc+1, cl_brc, result)
    if op_brc > cl_brc:
        get(str_+'(', n, op_brc+1, cl_brc, result)
        get(str_+')', n, op_brc, cl_brc+1, result)





result = []
get ("", 4, 0, 0, result)
print (result)