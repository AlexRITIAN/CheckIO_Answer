'''x --- 1
    o ----2
'''
def checkio(game_result):
    for num in range(0,3):
        if game_result[num][0] is game_result[num][1] and game_result[num][1] is game_result[num][2] and game_result[num][0] != '.':
            return game_result[num][0]
        elif game_result[0][num] is game_result[1][num] and game_result[1][num] is game_result[2][num] and game_result[0][num] != '.':
            return game_result[0][num]
    if game_result[0][0] is game_result[1][1] and game_result[1][1] is game_result[2][2] and game_result[0][0] != '.':
        return game_result[0][0]
    elif game_result[0][2] is game_result[1][1] and game_result[1][1] is game_result[2][0] and game_result[0][2] != '.':
        return game_result[0][2]
    return "D" 

def chickio_vol2(result):
    rows = result
    cols = map(''.join,zip(*rows))
    diags = map(''.join,zip(*[(r[i],r[2-i]) for i,r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    print(lines)
    return 'X' if ('XXX' in lines) else 'O' if('OOO' in lines) else 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
   
    print(checkio([".XO","X.X","OOO"]))
