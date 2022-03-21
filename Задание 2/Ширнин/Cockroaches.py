def Cockroaches(room):
    directions = ['L','D','R','U']
    holes = ['0','1','2','3','4','5','6','7','8','9']
    result = [0]*10
    r = room[0]
    for i in range(1,len(room)-1):
        r += room[i][len(room[i])-1] 
    for i in reversed(range(len(room[0]))):
        r += room[len(room)-1][i]
    for i in reversed(range(1,len(room)-1)):
        r += room[i][0] 
    r += r
    r = r[::-1]
    for i in range(len(room)):
        for j in range(len(room[i])):
            pos = 0
            if room[i][j] in directions:
                if room[i][j] == 'L':
                    pos = i-1
                elif room[i][j] == 'D':
                    pos = len(room)+j-2
                elif room[i][j] == 'R':
                    pos = 2*len(room)+len(room[i])-i-4
                elif room[i][j] == 'U':
                    pos = 2*len(room)+2*len(room[i])-j-5
                for k in range(pos,len(r)):
                    if r[k] in holes:
                        result[int(r[k])] += 1
                        break
    return(result)

room=["+----------------0---------------+",
      "|                                |",
      "|                                |",
      "|          U        D            |",
      "|     L                          |",
      "|              R                 |",
      "|           L                    |",
      "|  U                             1",
      "3        U    D                  |",
      "|         L              R       |",
      "|                                |",
      "+----------------2---------------+"]
Cockroaches(room)