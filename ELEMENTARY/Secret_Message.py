def find_message(text):
    message = ""
    for c in text:
        if c.isupper():
            message += c
    return message

'''filter'''
find_message_vol2 = lambda text: ''.join(filter(str.isupper, text))

'''not lambda'''
#this not use lambda,maybe clearer than lambda version
def find_message_vol3(text):
    return ''.join(c for c in text if c.isupper())
#find_message_1 = lambda text:(c + c) for c in text if c.isupper()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    # assert find_message("hello world!") == "", "Nothing"
    # assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    print(find_message_vol2("How are you? Eh, ok. Low or Lower? Ohhh."))
    print(find_message_vol3("How are you? Eh, ok. Low or Lower? Ohhh."))