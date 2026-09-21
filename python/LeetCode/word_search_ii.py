from CodingPractice.LeetCode.implement_trie import Trie
import copy


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        nrows, ncols = len(board), len(board[0])
        ans = []

        def dfs(cell_row, cell_col, node, visited):
            nonlocal ans
            if 0 <= cell_row < nrows and 0 <= cell_col < ncols and not visited[cell_row][cell_col]:
                new_visited = copy.deepcopy(visited)
                new_visited[cell_row][cell_col] = True
                next_node = node.get_child_with_letter(board[cell_row][cell_col])
                if next_node:
                    if next_node.terminate:
                        ans += [next_node.word]
                        next_node.terminate = False

                    dfs(cell_row + 1, cell_col, next_node, new_visited)
                    dfs(cell_row - 1, cell_col, next_node, new_visited)
                    dfs(cell_row, cell_col + 1, next_node, new_visited)
                    dfs(cell_row, cell_col - 1, next_node, new_visited)

        for row in range(nrows):
            for col in range(ncols):
                if len(ans) < len(words):
                    starting_node = trie.root.get_child_with_letter(board[row][col])
                    if starting_node:
                        initial_visited = [[False] * ncols for _ in range(nrows)]
                        dfs(row, col, trie.root, initial_visited)

        return ans


if __name__ == '__main__':
    board = [["a", "b"], ["c", "d"]]
    words = ["cdba"]
    sol = Solution()
    print(sol.findWords(board=board, words=words))
