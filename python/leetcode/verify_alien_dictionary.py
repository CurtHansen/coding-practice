from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.letter_ordering = dict(zip(list(order), list(range(len(order)))))
        self.words = words
        n = len(words)
        pairs = list(zip(list(range(n-1)),list(range(1,n))))

        for pair in pairs:
            result = self.check_pair(pair)
            if result is False:
                return False

        return True

    def check_pair(self, pair):
        word1, word2 = self.words[pair[0]], self.words[pair[1]]
        idx, n1, n2 = 0, len(word1), len(word2)
        while idx < n1 and idx < n2:
            if self.letter_ordering[word1[idx]] < self.letter_ordering[word2[idx]]:
                break
            elif self.letter_ordering[word1[idx]] > self.letter_ordering[word2[idx]]:
                return False
            elif idx == (min(n1,n2) - 1):
                if n1 <= n2:
                    break
                else:
                    return False

            idx += 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(sol.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
    print(sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
    print(sol.isAlienSorted(["ubg", "kwh"], "qcipyamwvdjtesbghlorufnkzx"))