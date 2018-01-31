'''
链接：https://www.zhihu.com/question/20197863/answer/68640989
羅馬數字共有7個，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）。

右加左減：
在較大的羅馬數字的右邊記上較小的羅馬數字，表示大數字加小數字。
在較大的羅馬數字的左邊記上較小的羅馬數字，表示大數字减小數字。
左减的数字有限制，仅限于I、X、C。
比如45不可以写成VL，只能是XLV。
但是，左減時不可跨越一個位數。
比如，99不可以用IC表示，而是用XCIX表示。（等同於阿拉伯數字每位數字分別表示。）
左減數字必須為一位，比如8寫成VIII，而非IIX。
右加數字不可連續超過三位，比如14寫成XIV，而非XIIII。（見下方“數碼限制”一項。）
加線乘千：在羅馬數字的上方加上一條橫線或者加上下標的Ⅿ，表示將這個數乘以1000，即是原數的1000倍。
同理，如果上方有兩條橫線，即是原數的1000000倍。

數碼限制：
同一數碼最多只能连续出現三次，如40不可表示為XXXX，而要表示為XL。
例外：由於IV是古羅馬神話主神朱庇特（即IVPITER，古羅馬字母裡沒有J和U）的首字，因此有時用IIII代替IV。'''
def checkio(data):
    numbers = [1000,500,100,50,10,5,1]
    romans = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
    result = []
    temp = len(numbers)
    for i in range(0,len(numbers)):
        #beacuse 0<data<=3999
        if i == temp:
            continue
        elif i%2 != 0 and  len(numbers) -1 > i > 0 and numbers[i-1] - data <= numbers[i+1]:
            result.append(romans[numbers[i + 1]] + romans[numbers[i - 1]])
            data = data % numbers[i + 1]
            temp = i + 1
            continue
        elif int(data/numbers[i]) == 4:
            result.append(romans[numbers[i]] + romans[5 * numbers[i]])
        else:
            result.append(romans[numbers[i]] * int(data/numbers[i]))
        data = data % numbers[i]
    return "".join(result)

def checkio_vol2(data):
    convert = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 
               90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman_result = ''
    while data > 0:
        for arab_number in reversed(list(convert.keys())):
            if data >= arab_number:
                data -= arab_number
                roman_result += convert[arab_number]
                break
    return roman_result

#I dont understand how it work
def checkio(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(6) == 'VI', '6'
    # assert checkio(76) == 'LXXVI', '76'
    # assert checkio(499) == 'CDXCIX', '499'
    # assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print(checkio(6))
    print(checkio(76))
    print(checkio(499))
    print(checkio(3888))