from collections import deque
from string import ascii_lowercase
from collections import defaultdict
from typing import List


class Solution:
    def find_neighbors(self, word):
        for pos in range(len(word)):
            for letter in ascii_lowercase:
                candidate_word = word[:pos] + letter + word[pos+1:]
                if candidate_word in self.word_set:
                    self.graph[word].add(candidate_word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.word_set = set(wordList)
        self.word_set.add(beginWord)
        self.graph = defaultdict(set)
        self.visited = set()

        for word in self.word_set:
            self.find_neighbors(word)

        myqueue = deque()
        myqueue.append((beginWord, 1))
        while len(myqueue) > 0:
            word, numsteps = myqueue.popleft()
            self.visited.add(word)
            for transition_word in self.graph[word]:
                if transition_word == endWord:
                    return numsteps + 1
                if transition_word not in self.visited:
                    myqueue.append((transition_word, numsteps + 1))
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit","cog",["hot","cot","dot","tog","cog"]))