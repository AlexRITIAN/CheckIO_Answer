def checkio(text,words):
    return sum(word in text.lower() for word in words)

if __name__ == '__main__':
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print(checkio("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    print(checkio("Bananas, give me bananas!!!", {"banana", "bananas"}))
    print(checkio("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}))