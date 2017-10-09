def checkio(*args):
    if len(args) == 0:
        return 0
    return sorted(args,reverse=True)[0] - sorted(args,reverse=False)[0]

if __name__ == "__main__":
    print(checkio(0.0015,0.0025,0.0035))