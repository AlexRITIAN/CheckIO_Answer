from math import fabs
from functools import partial

def checkio(numbers_array):
    l = list(numbers_array)
    for n in range(len(l) - 1,0,-1):
        for i in range(0,n):
            if fabs(l[i]) > fabs(l[i+1]):
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l

test = partial(sorted,key=abs)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    # assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    # assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    # assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print(check_it(checkio((1,2,3,0))))
    print(check_it(test((1,2,3,0))))
