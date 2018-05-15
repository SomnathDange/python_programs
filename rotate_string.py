def fun(str,opr):
    if opr[2] is 'L':
        res=le1(str,opr)
    else:
        res=r1(str,opr)
    return res

def le1(str,opr):
    new_str=list(str)
    for x in range(opr[0],opr[1]+1):
        if(new_str[x] == 'a'):
            new_str[x]='z'
        else:
            new_str[x]=chr(ord(new_str[x]) - 1)

    return new_str

def r1(str,opr):
    new_str=list(str)
    for x in range(opr[0],opr[1]+1):
        if(new_str[x] == 'z'):
            new_str[x]='a'
        else:
            new_str[x]=chr(ord(new_str[x]) + 1)

    return new_str
               


str1=fun("abc",[0,1,'L'])
str2=fun(str1,[1,2,'R'])
print fun(str2,[0,2,'R'])

