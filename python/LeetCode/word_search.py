class Solution:
    def get_starting_points(self, board, char):
        ans = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                if board[i][j] == char:
                    ans.append([i, j])

        return ans

    def explore_from_point(self, board, word, start_point):
        visited = [[False] * self.ncols for _ in range(self.nrows)]

        def recursive_search(cell, charidx, visited_nodes):
            visited_nodes = [row[:] for row in visited_nodes]  # create local copy
            print(f'Checking cell/charidx/visited_nodes {cell}/{charidx}/{visited_nodes}')
            if cell[0] < 0 or cell[0] >= self.nrows or cell[1] < 0 or cell[1] >= self.ncols:
                return
            if visited_nodes[cell[0]][cell[1]]:
                print(f'Rejecting cell/charidx {cell}/{charidx} because already visited.')
                return
            if board[cell[0]][cell[1]] != word[charidx]:
                return
            if charidx == self.nchars - 1:
                self.found = True
                return

            print(f'For cell/charidx {cell}/{charidx} going one level deeper')
            visited_nodes[cell[0]][cell[1]] = True
            for x, y in [[-1, 0], [+1, 0], [0, -1], [0, +1]]:
                if self.found:
                    break
                recursive_search([cell[0] + x, cell[1] + y], charidx + 1, visited_nodes)

        recursive_search(start_point, 0, visited)

    def exist(self, board, word: str) -> bool:

        self.found = False
        self.nchars = len(word)
        self.nrows = len(board)
        self.ncols = len(board[0])

        starting_points = self.get_starting_points(board, word[0])
        for start_point in starting_points:
            if self.found:
                break
            self.explore_from_point(board, word, start_point)

        return self.found


if __name__ == '__main__':
    sol = Solution()
    myboard = [["A", "B", "C", "E"],
               ["S", "F", "E", "S"],
               ["A", "D", "E", "E"]]
    mystring = "ABCESEEEFS"
    print(sol.exist(myboard, mystring))
