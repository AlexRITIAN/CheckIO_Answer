def checkio(*args):
    if len(args) == 0:
        return 0
    return sorted(args,reverse=True)[0] - sorted(args,reverse=False)[0]