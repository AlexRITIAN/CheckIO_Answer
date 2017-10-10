def checkio(*args):
    if len(args) == 0:
        return 0
    return sorted(args,reverse=True)[0] - sorted(args,reverse=False)[0]

def checkio_vol1(*args):
    return max(args) - min(args) if args else 0

def checkio_vol2(*args):
    return len(args) and max(args) - min(args)

if __name__ == "__main__":
    print(checkio_vol1(0.0015,0.0025,0.0035))