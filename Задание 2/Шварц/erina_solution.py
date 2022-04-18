def very_even(n):
    try:
        if len(str(n)) == 1:
            if (int(n) % 2 == 0) or (int(n) == 0):
                return True
            else:
                return False
        else:
            num = 0
            n = str(n)
            for x in n:
                num = num + int(x)
            return very_even(num)
    except ValueError:
        return "Введено недопустимое значение"
