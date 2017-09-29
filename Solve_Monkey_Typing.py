def count_words(text, words):
    sum = 0
    for word in words:
        if(word in text.lower()):
            sum = sum + 1
            #print(word)
    return sum

def checkio_vol2(text,words):
    return sum(word in text.lower() for word in words)


if __name__ == '__main__':
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
    print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}))