
def getResult(args,key,flag):
    result = 0
    first_flag = True
    if flag:
        if key == None:
            if len(args) == 1:
                for arg in args[0]:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif arg > result:
                        result = arg
            else:
                for arg in args:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif arg > result:
                        result = arg
        else:
            if len(args) == 1:
                for arg in args[0]:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif key(arg) > key(result):
                        result = arg
            else:
                for arg in args:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif key(arg) > key(result):
                        result = arg
    else:
        if key == None:
            if len(args) == 1:
                for arg in args[0]:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif arg < result:
                        result = arg
            else:
                for arg in args:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif arg < result:
                        result = arg
        else:
            if len(args) == 1:
                for arg in args[0]:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif key(arg) < key(result):
                        result = arg
            else:
                for arg in args:
                    if first_flag:
                        result = arg
                        first_flag = False
                    elif key(arg) < key(result):
                        result = arg
                
    return result


def max(*args,key=None):
    return getResult(args,key,True)

def min(*args,key=None):
    return getResult(args,key,False)

if __name__ == "__main__":
    print(max(1.2,1.1,2.1,2.2,key=int))
    print(min(1.2,1.1,2.1,2.2,key=int))
    print(max(1.2,1.1,2.1,2.2))
    print(min(1.2,1.1,2.1,2.2))
    print(max([1.2,1.1,2.1,2.2],key=int))
    print(min([1.2,1.1,2.1,2.2],key=int))
    print(max([1.2,1.1,2.1,2.2]))
    print(min([1.2,1.1,2.1,2.2]))