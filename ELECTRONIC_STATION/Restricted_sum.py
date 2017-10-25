def checkio(data):
    temp = 0
    n = 0
    return calcultator(data,temp,n)

def calcultator(data,temp,n):
    if(n == len(data)):
        return temp
    else:
        temp = temp + data[n]
        n = n + 1
        return calcultator(data,temp,n)

def checkio_vol2(data,idx=0):
    if idx>=len(data):
        return 0
    return data[idx] + checkio_vol2(data,idx+1)

if __name__ == "__main__":
    print(checkio([1,2,3]))