def tpl_sort(a):
    for i in a:
        if not isinstance(i,int):
            return tuple(a)
    return tuple(sorted(a))


a=(5,3,6,72,1)
b=(8,45,8,5.1)
print(tpl_sort(a)) #(1, 3, 5, 6, 72)
print(tpl_sort(b)) #(8, 45, 8, 5.1)

