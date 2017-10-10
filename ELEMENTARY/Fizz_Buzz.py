def checkio(number):
    return "Fizz Buzz" if number%3 == 0 and number%5 ==0 else "Fizz" if number%3 == 0 else "Buzz" if number%5 ==0 else str(number)

def checkio_vol2(number):
    if number % 15 == 0:
        return "Fizz Buzz"
    if number % 5 == 0:
        return "Fizz"
    if number % 3 == 0:
        return "Buzz"
    return str(number)

def checkio_vol3(number):
    return 'Fizz' * (not number % 3) + ' ' * (not number % 15) + 'Buzz' * (not number % 5) or str(number)

if __name__ == "__main__":
    print(checkio_vol3(15))