def canWinNim(n: int) -> bool:
    canwin = dict()
    canwin[1] = True
    canwin[2] = True
    canwin[3] = True

    def check(start: n) -> bool:
        results = []
        for attempt in [1, 2, 3]:
            results.append(canwin[start-attempt])
        #print("start {} / results {} / ~all(results) {}".format(start, results, not all(results)))
        return not all(results)

    for i in range(4, n+1):
        canwin[i] = check(i)

    return canwin[n]


if __name__ == '__main__':
    for j in range(1, 11):
        print(canWinNim(j))