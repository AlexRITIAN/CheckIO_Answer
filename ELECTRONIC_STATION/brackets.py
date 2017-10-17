def checkio(expression):
    brackets = []
    for char in expression:
        if char == "{" or char == "[" or char =="(" or char == ")" or char == "]" or char == "}":
            brackets.append(char)
    if len(brackets)%2 != 0:
        return False
    for i in range(0,int(len(brackets)/2)):
        if not(brackets[i] == "{" and brackets[len(brackets)-1 - i] == "}") and not(brackets[i] == "[" and brackets[len(brackets)-1 - i] == "]") and not(brackets[i] == "(" and brackets[len(brackets)-1 - i] == ")"):
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
    print(checkio("((5+3)*2+1)"))
    print(checkio("[1+1]+(2*2)-{3/3}"))