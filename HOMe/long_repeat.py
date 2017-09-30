from itertools import groupby
def long_repeat(line):
    result = []
    temp = ""
    num = 0
    for char in line:
        if temp is char:
            num += 1
        else:
            temp = char
            result.append(num)
            num = 1
    result.append(num)
    return sorted(result,reverse=True)[0] if line != "" else 0

def long_repeat_vol2(line):
    return max((sum(1 for _ in g) for k,g in groupby(line)),default=0)
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert long_repeat('sdsffffse') == 4, "First"
    #assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print(long_repeat('aa'))
    print(long_repeat_vol2('ddvvrwwwrggg'))