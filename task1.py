def calculator(f_num,s_num,oper):
    if oper=='+':
        return f_num+s_num
    elif oper=='-':
        return f_num-s_num
    elif oper=='/':
        try:
            return f_num / s_num
        except:
            return 'Нельзя разделить на ноль'
    elif oper=='*':
        return f_num / s_num



print(calculator(5,0,'/')) #Нельзя разделить на ноль
print(calculator(20,20,'+')) #40
