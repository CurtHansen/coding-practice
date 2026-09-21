# Implementation of a disjoint set union data structure (DSU).


class DSU():
    def __init__(self, N):
        self.parents = list(range(N))

    def __get_root(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return self.parents[x]

    def find(self, x, y):
        # Determine if x and y belong to same group.
        root_x = self.__get_root(x)
        root_y = self.__get_root(y)
        return root_x == root_y

    def union(self, x, y):
        # Set root of x to be root of y.
        root_x = self.__get_root(x)
        root_y = self.__get_root(y)
        self.parents[root_x] = root_y


if __name__ == '__main__':
    nmembers = 10
    dsu_set = DSU(nmembers)
    print(dsu_set.parents)
    print(dsu_set.find(0,7))
    dsu_set.union(0,7)
    print(dsu_set.find(0,7))
    print(dsu_set.parents)
    dsu_set.union(0,4)
    print(dsu_set.parents)

