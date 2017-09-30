def get_first_from_sorted(args,key,flag):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args,key=key,reverse=flag)[0]
                

def min(*args, key=None):
    return get_first_from_sorted(args, key, False)

def max(*args, key=None):
    return get_first_from_sorted(args, key, True)


if __name__ == "__main__":
    print(max(1,2,6,4,5))
    print(min([1,2,3,4,5]))
    print(max(2.1,5.6,5.9,key=int))
    