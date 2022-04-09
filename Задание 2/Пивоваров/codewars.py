def digital_root(n):
    rez = 0
    text = str(n)

    while len(text) > 1:
        for i in range(len(text)):
            rez += int(text[i])

        if len(str(rez)) > 1:
            text = str(rez)

        if len(str(rez)) == 1:
            text = str(rez)
            
        rez = 0 
    
    return(int(text))
