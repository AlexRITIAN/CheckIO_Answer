checkio = lambda s: not(

        len(s) < 10

        or s.isdigit()

        or s.isalpha()

        or s.islower()

        or s.isupper()

    ) 


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print(checkio('A1213pokl'))
    print(checkio('bAse730onE4'))
    print(checkio('asasasasasasasaas'))
    print(checkio('QWERTYqwerty'))
    print(checkio('123456123456'))
    print(checkio('QwErTy911poqqqq'))
