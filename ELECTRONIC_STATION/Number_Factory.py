def checkio(number):
    pNumbers = []
    pFlag = True
    resultNmbers = []
    wFlag = False
    for i in range(2,number + 1):
        for j in range(2,i + 1):
            if i % j == 0:
                if i != j and j != 1:
                    pFlag = False
                elif i == j and pFlag:
                    pNumbers.append(i)
    while (True):
        for p in pNumbers:
            if number % p == 0 and number:
                resultNmbers.append(p)
                number = number / p
                break
            elif p > number:
                wFlag = True
                break
        if wFlag:
            break
    print(resultNmbers)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    checkio(20)
    # checkio(21)
    # checkio(17)
    # checkio(33)
    # checkio(3125)
    # checkio(9973) 