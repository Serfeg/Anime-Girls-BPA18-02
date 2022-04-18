def solution(n):  
    oneS = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tenS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thouS = ["", "M", "MM", "MMM", "MMMM"]
    
    thou = thouS[n // 1000]
    hund = hundS[n // 100 % 10]
    ten = tenS[n // 10 % 10]
    one =  oneS[n % 10]
    
    return thou + hund + ten + one