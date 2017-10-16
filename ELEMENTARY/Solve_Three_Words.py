def checkio(words):
    n = 0
    for s in words.split():
        if s.isalpha():
            n += 1
        elif n >= 3:
            break
        else:
            n = 0
    return n >= 3

def checkio_vol2(words):
    n = 0
    for s in words.split():
        n = (n + 1)*s.isalpha()
        if n == 3: 
            return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("Hello World hello") == True, "Hello"
    # assert checkio("He is 123 man") == False, "123 man"
    # assert checkio("1 2 3 4") == False, "Digits"
    # assert checkio("bla bla bla bla") == True, "Bla Bla"
    # assert checkio("Hi") == False, "Hi"
    # print(checkio("Hello World hello"))
    # print(checkio("He is 123 man"))
    # print(checkio("1 2 3 4"))
    # print(checkio("bla bla bla bla"))
    # print(checkio("Hi"))
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
    print(checkio_vol2("one two 3 four five six 7 eight 9 ten eleven 12"))