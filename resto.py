i = 2
while i <= 5:
    j = i
    while j <= 5:
        a = i
        b = j
        resto = a % b
        while resto != 0:
            a = b
            b = resto
            resto = a % b
        if b == 1:
            print(i, ',', j)
        j += 1
    i += 1