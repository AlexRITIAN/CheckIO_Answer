def checkio(expression):
    comparison = {"(":")","[":"]","{":"}"}
    brackets = []
    for char in expression:
        if char in comparison or char in comparison.values():
            brackets.append(char)
    if len(brackets)%2 != 0:
        return False
    l = int(len(brackets)/2)
    for n in range(0,l - 1):
        if brackets[l - 1 -n] in comparison:
            if brackets[l + n] != comparison[brackets[l - 1 - n]]:
                print(l)
                print(n)
                print(brackets[l + n])
                print(comparison[brackets[l - 1 - n]])
                return False
        elif brackets[l + n] not in comparison:
            print(l)
            print(n)
            print(brackets[l + n])
            return False
        elif brackets[l -1 -n] != comparison[brackets[l + n]]:
            print(l)
            print(n)
            print(brackets[l -1 -n])
            print(comparison[brackets[l + n]])
            return False
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("((5+3)*2+1)") == True, "Simple"
    # assert checkio("{[(3+1)+2]+}") == True, "Different types"
    # assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    # assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    # assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    # assert checkio("2+3") == True, "No brackets, no problem"
    # print(checkio("((5+3)*2+1)"))
    print(checkio("[1+1]+(2*2)-{3/3}"))
    # print(checkio("(3+{1-1)}"))