from collections import defaultdict


def numDirections(trajectory):
    n = len(trajectory)
    print(n)
    changes = defaultdict(int)
    xchanges,ychanges = [],[]
    for i in range(1,n):
        xchange = 0 if trajectory[i][0]==trajectory[i-1][0] else (trajectory[i][0]-trajectory[i-1][0])/abs((trajectory[i][0]-trajectory[i-1][0]))
        xchanges.append(xchange)
        ychange = 0 if trajectory[i][1]==trajectory[i-1][1] else (trajectory[i][1]-trajectory[i-1][1])/abs((trajectory[i][1]-trajectory[i-1][1]))
        ychanges.append(ychange)
    print(xchanges)
    print(ychanges)
    print(' ')
    num_changes = 0
    for i in range(1,n-1):
        if xchanges[i]!=xchanges[i-1] or ychanges[i]!=ychanges[i-1]:
            changes[(xchanges[i],xchanges[i-1],ychanges[i],ychanges[i-1])] += 1
    for c in changes.items():
        print(c)
    return num_changes


if __name__ == '__main__':
    points = [[13, 6], [5, 14], [7, 15], [13, 13], [3, 15], [8, 9],
     [9, 8], [2, 8], [6, 6], [10, 9], [2, 12], [2, 5],
     [14, 3], [11, 11], [2, 12], [3, 7], [9, 9], [15, 4],
     [10, 15], [12, 14], [3, 7], [4, 5], [5, 10], [1, 14],
     [3, 12], [13, 6], [8, 10], [15, 5], [13, 12], [8, 13],
     [8, 15], [3, 15], [11, 15], [5, 2], [3, 1], [14, 4],
     [15, 9], [6, 7], [10, 13]]

    print(numDirections(points))