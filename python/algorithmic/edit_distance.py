def edit_distance(stringfrom, stringto):
    lsfrom, lsto = len(stringfrom), len(stringto)
    dptable = [[float('inf')] * (lsfrom+1) for _ in range(lsto+1)]

    for i in range(lsto+1):
        dptable[i][0] = i
    for j in range(lsfrom+1):
        dptable[0][j] = j

    for i in range(1, lsto+1):
        for j in range(1, lsfrom+1):
            latests1char = stringto[i-1]
            latests2char = stringfrom[j-1]
            matchpenalty = 0 if latests1char == latests2char else 1
            dptable[i][j] = min(dptable[i-1][j-1] + matchpenalty,
                                dptable[i-1][j] + 1,
                                dptable[i][j-1] + 1)

    for i in range(lsto+1):
        print(dptable[i])
    return dptable[lsto][lsfrom]


if __name__ == '__main__':
    s1 = 'dogs'
    s2 = 'dogshit'
    print(edit_distance(s1, s2))
