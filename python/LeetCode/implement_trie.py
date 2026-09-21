# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Node:

    def __init__(self, letter=None):
        self.letter = letter
        self.children = []
        self.terminate = False
        self.word = None

    def get_child_with_letter(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child
        return None


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        letters = list(word)
        current_node = self.root

        def find_node(parent_node, letter):
            for child in parent_node.children:
                if child.letter == letter:
                    return child
            return None

        for idx, letter in enumerate(letters):
            child_node = find_node(current_node, letter)
            if child_node is None:
                child_node = Node()
                child_node.letter = letter
                current_node.children.append(child_node)
            current_node = child_node
            if idx == len(letters) - 1:
                current_node.terminate = True
                current_node.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        letters_to_search = list(word)
        ans = False

        def recur(current_node, remaining_letters):
            if len(remaining_letters) == 0:
                if current_node.terminate is True:
                    nonlocal ans
                    ans = True
            else:
                for each_child in current_node.children:
                    if remaining_letters[0] == each_child.letter:
                        recur(each_child, remaining_letters[1:])

        recur(self.root, letters_to_search)

        return ans

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        letters_to_search = list(prefix)
        ans = False

        def recur(current_node, remaining_letters):
            if len(remaining_letters) == 0:
                nonlocal ans
                ans = True
            else:
                letter_to_search = remaining_letters[0]
                remaining_letters = remaining_letters[1:]
                for each_child in current_node.children:
                    if letter_to_search == each_child.letter:
                        recur(each_child, remaining_letters)

        recur(self.root, letters_to_search)

        return ans


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
    print(trie.search("doggy"))
    print(trie.startsWith("doggy"))
    trie.insert("dog")
    print(trie.search("doggy"))
    print(trie.search("dog"))
    trie.insert("doggy")
    print(trie.search("doggy"))

