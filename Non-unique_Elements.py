#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    result = []
    for item in data:
        if(data.count(item) != 1):
            result.append(item)
    return result

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    print("It is all good. Let's check it now")
    print(list(checkio([1, 2, 3, 1, 3])))
    print(list(checkio([1, 2, 3, 4, 5])))
    print(list(checkio([5, 5, 5, 5, 5])))
    print(list(checkio([10, 9, 10, 10, 9, 8])))