def find_message(text):
    message = ""
    for c in text:
        if c.isupper():
            message += c
    return message

#find_message_1 = lambda text:(c + c) for c in text if c.isupper()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    # assert find_message("hello world!") == "", "Nothing"
    # assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))