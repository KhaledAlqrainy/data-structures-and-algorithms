
def validate_brackets(data):

    open = ['{','(','[']
    close = ['}',')',']']
    list=[] 

    for i in data:
        
        if i in open:
            list.append(i) 
        elif i in close:
            index=close.index(i) 
            if len(list)>0 and open[index]==list[len(list)-1]:
                list.pop()
            else:
                return False
            
    if len(list)==0:
        return True
    else:
        return False