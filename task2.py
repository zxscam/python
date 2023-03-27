def slicer(tpl,elem):
    if elem in tpl:
        if tpl.count(elem)>1:
                f_ind=tpl.index(elem)
                s_ind=tpl.index(elem, f_ind+1)+1
                return tpl[f_ind:s_ind]
        else:
            return tpl[tpl.index(elem):]
    else:
        return()


a=(1,45,32,4,46,346,3,5,6,4,4)
b=4
print(slicer(a,b)) #(4, 46, 346, 3, 5, 6, 4)