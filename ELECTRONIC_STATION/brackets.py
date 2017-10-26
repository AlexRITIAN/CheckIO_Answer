def checkio(expression):
    comparison = {"(":")","[":"]","{":"}"}
    brackets = []
    try:
        for char in expression:
            if char in comparison:
                brackets.append(char)
            elif char in comparison.values():
                if char == comparison[brackets[-1]]:
                    brackets.pop()
                else:
                    brackets.append(char)
    except:
        return False
    return len(brackets) == 0

def checkio_vol2(expression):
    comparison = {"(":")","[":"]","{":"}"}
    brackets = [""]
    try:
        for char in expression:
            if char in comparison:
                brackets.append(comparison[char])
            elif char in comparison.values() and char !=brackets.pop():
                return False
    except:
        return False
    return brackets == [""]
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("((5+3)*2+1)") == True, "Simple"
    # assert checkio("{[(3+1)+2]+}") == True, "Different types"
    # assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    # assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    # assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    # assert checkio("2+3") == True, "No brackets, no problem"
    # print(checkio("((5+3)*2+1)"))
    print(checkio("(((([[[{{{3}}}]]]]))))"))
    # print(checkio("(3+{1-1)}"))