def checkio(number):
    temp = 1
    for n in str(number):
        if n != '0':
            temp = temp * int(n)
    return temp

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(123405) == 120
    # assert checkio(999) == 729
    # assert checkio(1000) == 1
    # assert checkio(1111) == 1
    print(checkio(123405))
    print(checkio(999))
    print(checkio(1000))
    print(checkio(1111))