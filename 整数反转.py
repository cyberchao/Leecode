def reverse(x):
    li = list(str(x))
    if li[0] == '-':
        li.remove('-')
        li.reverse()
        stry = '-'+''.join(li)
        newx = int(stry)
        if newx < -2**31:
            return 0
        else:
            return newx
    else:
        li.reverse()
        stry = ''.join(li)
        newx = int(stry)
        if newx > 2**31-1:
            return 0
        else:
            return newx


reverse(-120)
