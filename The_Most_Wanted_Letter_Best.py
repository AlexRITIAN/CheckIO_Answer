

import string


def checkio(text):

    """

    We iterate through latyn alphabet and count each letter in the text.

    Then 'max' selects the most frequent letter.

    For the case when we have several equal letter,

    'max' selects the first from they.

    """

    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)

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