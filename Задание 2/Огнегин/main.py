def domain_name(a):
    n = len(a)
    res = ''
    if len(a) > 0:
        b = a.replace('http://','')
        b = b.replace('https://','')
        b = b.replace('www.','')
    for x in range(0,len(b),1):
        if b[x] == '.':
            break
        else:
            res += b[x]
    if len(a) == 0:
        return ''
    else:
        return res
