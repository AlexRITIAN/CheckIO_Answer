def chechio(pawns):
    pawns_postions = set((int(pawn[1]) - 1,ord(pawn[0]) - 97) for pawn in pawns)
    n = 0
    for r,c in pawns_postions:
        if (r - 1,c - 1) in pawns_postions or (r - 1,c + 1) in pawns_postions:
            n += 1
    return n
