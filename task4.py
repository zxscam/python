def del_from_tuple(tpl,elem):
    for elem in tpl:
        elem_ind = tpl.index(elem)
        return tpl[:elem_ind]+tpl[elem_ind+1:]
    return tpl

a=(5,3,2,5,1,12,5,1,5,2,6,32,5)
b=5
print(del_from_tuple(a,b)) #(3, 2, 5, 1, 12, 5, 1, 5, 2, 6, 32, 5)
