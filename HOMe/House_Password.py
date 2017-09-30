import re


DIGIT_RE = re.compile('\d')

UPPER_CASE_RE = re.compile('[A-Z]')

LOWER_CASE_RE = re.compile('[a-z]')


def checkio_re(data):

    """

    Return True if password strong and False if not

    

    A password is strong if it contains at least 10 symbols,

    and one digit, one upper case and one lower case letter.

    """

    if len(data) < 10:

        return False

    

    if not DIGIT_RE.search(data):

        return False


    if not UPPER_CASE_RE.search(data):

        return False


    if not LOWER_CASE_RE.search(data):

        return False

        

    return True


def checkio(data):

    #replace this for solution
    digitflag = False
    lowerflag = False
    upperflag = False
    if(len(data) >=10):
        for item in data:
            if(item.isdigit()):
                digitflag = True
            if(item.islower()):
                lowerflag = True
            if(item.isupper()):
                upperflag = True
            if(digitflag and lowerflag and upperflag):
                return True
    return False

checkio_shor = lambda s: not(

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
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print(checkio('A1213pokl'))
    print(checkio('bAse730onE4'))
    print(checkio('asasasasasasasaas'))
    print(checkio('QWERTYqwerty'))
    print(checkio('123456123456'))
    print(checkio('QwErTy911poqqqq'))
