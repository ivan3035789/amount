start = int(input())
summa = 0
if start == 0:
    print(summa)
else:
    i = int(input())
    summa = start + i
    while i != 0:
        if i == 0:
            print(summa)
        else:
            i = int(input())
        summa += i
    print(summa)