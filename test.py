from inspect import isgeneratorfunction

def substrings(string):
    l = len(string)
    for n in range(l, 0, -1):
        for i in range(l - n + 1):
            yield string[i:n+i]

def longest_palindromic(string):
    return next(sub for sub in substrings(string))

if __name__ == "__main__":
    # for str in substrings("abcd"):
        # print(str)
    # print(longest_palindromic("abcd"))
    for sub in substrings("abarada"):
        print(sub)

