def max(iterable,*[key]):
    nmax = 0
    temp = ""
    flag = false
    firstFlag = True
    for n in iterable:
        if isinstance(n,int):
            flag = True
            if firstFlag:
                nmax = n
                firstFlag = False
            elif n > nmax:
                nmax = n
                
        else:
            if firstFlag:
                nmax = ord(n)
                temp = n
            elif ord(n) > nmax:
                nmax = ord(n)
                temp = n
    return nmax if flag else temp

if __name__ == "__main__"
    