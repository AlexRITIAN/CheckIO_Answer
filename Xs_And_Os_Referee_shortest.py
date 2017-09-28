
def chick_io(result):
    rows = result
    cols = map(''.join,zip(*rows))
    diags = map(''.join,zip(*[(r[i],r[2-i]) for i,r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    print(lines)
    return 'X' if ('XXX' in lines) else 'O' if('OOO' in lines) else 'D'

if __name__ == "__main__":
    print(chick_io([".XO","X.X","OOO"]))
        