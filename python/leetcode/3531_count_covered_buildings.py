from collections import defaultdict
import sys
from typing import List
import matplotlib.pyplot as plt


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min = defaultdict(lambda: sys.maxsize)
        row_max = defaultdict(lambda: -sys.maxsize)
        col_min = defaultdict(lambda: sys.maxsize)
        col_max = defaultdict(lambda: -sys.maxsize)

        for c, r in buildings:
            row_min[r] = min(row_min[r], c)
            row_max[r] = max(row_max[r], c)
            col_min[c] = min(col_min[c], r)
            col_max[c] = max(col_max[c], r)

        def debug(dictionary, title):
            print(f'\n{title}:')
            for k in sorted(dictionary.keys()):
                print(f'{k}: {dictionary[k]}')

        debug(row_min,'row_min')
        debug(row_max,'row_max')
        debug(col_min,'col_min')
        debug(col_max,'col_max')

        count = 0
        interior = []
        for c, r in buildings:
            if (row_min[r] < c) and (row_max[r] > c) and (col_min[c] < r) and (col_max[c] > r):
                count += 1
                interior.append([c,r])

        plot_points(buildings, n, interior)

        return count


def plot_points(points, n, interior=None):
    """
    points: list of [x, y]
    interior: subset of points to be colored blue
    n: grid size (plot will show 0..n on each axis)
    """
    interior = set(map(tuple, interior or []))

    xs_blue, ys_blue = [], []
    xs_red, ys_red = [], []

    for x, y in points:
        if (x, y) in interior:
            xs_blue.append(x)
            ys_blue.append(y)
        else:
            xs_red.append(x)
            ys_red.append(y)

    plt.figure(figsize=(6, 6))
    plt.scatter(xs_red, ys_red, color='red')    # red points (default)
    plt.scatter(xs_blue, ys_blue, color='blue')  # blue points

    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.xticks(range(0, n + 1))
    plt.yticks(range(0, n + 1))
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == '__main__':
    sol = Solution()
    data = (20,[[12,4],[6,18],[4,9],[11,5],[11,14],[13,8],[6,2],[6,20],[4,2],[17,5],[19,2],[9,1],[15,7],[18,3],[7,3],[18,12],[8,4],[9,12],[15,9],[16,8],[3,1],[5,7],[11,2],[5,16],[4,18],[9,14],[16,1],[10,15],[15,11],[18,7],[2,20],[12,6],[14,12],[5,18],[9,16],[10,8],[1,5],[16,3],[8,20],[18,9],[20,12],[4,4],[7,11],[20,5],[12,19],[19,15],[1,9],[2,17],[16,16],[12,3],[20,16],[14,9],[4,8],[19,8],[1,2],[2,1],[10,14],[6,10],[20,9],[6,19],[20,18],[7,18],[3,11],[8,1],[19,10],[1,4],[5,20],[17,6],[8,3],[2,5],[11,17],[2,14],[15,17],[4,5],[17,8],[8,5],[8,14],[19,14],[15,10],[20,6],[7,6],[12,11],[4,16],[17,1],[19,7],[9,6],[3,20],[17,19],[10,13],[15,12],[7,8]])
    print(sol.countCoveredBuildings(*data))