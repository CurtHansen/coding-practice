# See https://leetcode.com/problems/dungeon-game/


def calculateMinimumHP(dungeon):

    nrows = len(dungeon)
    ncols = len(dungeon[0])
    min_incoming_needed = [[float('inf')] * ncols for _ in range(nrows)]

    min_incoming_needed[nrows-1][ncols-1] = 1 - dungeon[nrows-1][ncols-1]

    for idx in range(ncols-2, -1, -1):
        min_incoming_needed[nrows-1][idx] = max(1 - dungeon[nrows-1][idx],
                                                min_incoming_needed[nrows-1][idx+1] - dungeon[nrows-1][idx])
    for idx in range(nrows-2, -1, -1):
        min_incoming_needed[idx][ncols-1] = max(1 - dungeon[idx][ncols-1],
                                                min_incoming_needed[idx+1][ncols-1] - dungeon[idx][ncols-1])

    for i in range(nrows-2, -1, -1):
        for j in range(ncols-2, -1, -1):
            min_incoming_needed[i][j] = max(1 - dungeon[i][j],
                                            min(-dungeon[i][j] + min_incoming_needed[i][j+1],
                                                -dungeon[i][j] + min_incoming_needed[i+1][j]))

    return max(1, min_incoming_needed[0][0])


if __name__ == '__main__':
    dungeon = [[1,-4,5,-99],[2,-2,-2,-1]]
    print(calculateMinimumHP(dungeon))