def validSolution(SudokuSolution):

    for i in range(len(SudokuSolution)):
        horizontal = 0
        vertical = 0
        for j in range(len(SudokuSolution)):
            #вертикальная проверка
            if isinstance(SudokuSolution[j][i], str) :
                return False
            vertical += SudokuSolution[j][i]
            #горизонтальная проверка
            if isinstance(SudokuSolution[i][j], str):
                return False
            horizontal += SudokuSolution[i][j]
            #проверка номеров
            if SudokuSolution[i][j] < 1 or SudokuSolution[i][j] > 9:
                return False
        if vertical != 45 or horizontal != 45:
            # print (vertical)
            # print (horizontal)
            return False

    return True 