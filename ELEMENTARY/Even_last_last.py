def checkio(array):
    sum = 0
    for index in range(0,len(array),2):
        sum += array[index]
    return sum * array[len(array) - 1]

def checkio_vol2(array):
    if len(array) == 0:
        return 0
    return sum(array[i] for i in list(range(0,len(array),2))) * array[len(array) - 1]

def checkio_vol3(array):
    return sum(array[0::2]) * array[-1] if array else 0

if __name__ == '__main__':
    print(checkio_vol3([0,1,2,3,4,5]))