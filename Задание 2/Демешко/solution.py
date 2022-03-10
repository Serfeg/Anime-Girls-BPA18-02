def odd_row(n):
    res = []
    s = n**2 - (n//2) * 2 
    if s % 2 == 0:
        s += 1
    
    while len(res) < n:
        res.append(s)
        s += 2
        
    return res