
checkio = lambda data:[item for item in data if data.count(item) > 1]

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print("It is all good. Let's check it now")
    print(list(checkio([1, 2, 3, 1, 3])))
    print(list(checkio([1, 2, 3, 4, 5])))
    print(list(checkio([5, 5, 5, 5, 5])))
    print(list(checkio([10, 9, 10, 10, 9, 8])))