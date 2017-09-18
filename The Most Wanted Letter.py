import string

def checkio(text):
    text = text.lower()
    return min([(-1*text.count(ch),ch)for ch in string.ascii_lowercase])[1]

tests = [
    "Lorem ipsum dolor sit amet",
    "Aaaaaaaaaaaaaaaa!!!!",
    "Gregor then turned to look out the window at the dull weather.",
    "Nooooooooooo!!! Why!?!",
    "fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,"
]

for t in tests:
    ans = checkio(t)
    print('{{"input": "{0}", "answer": "{1}"}},'.format(t, ans))