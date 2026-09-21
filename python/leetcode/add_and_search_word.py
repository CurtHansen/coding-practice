class TrieNode:
    def __init__(self, letter=None):
        self.letter = letter
        self.children = []
        self.string = ''


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        def get_child_node_with_char(node, letter):
            for child in node.children:
                if child.letter == letter:
                    return child
            new_node = TrieNode(letter)
            node.children.append(new_node)
            return new_node

        def recur_add(node, pos):
            child_node = get_child_node_with_char(node, word[pos])
            if pos == len(word) - 1:
                child_node.string = word
            else:
                recur_add(child_node, pos + 1)

        current_node = self.root
        recur_add(current_node, 0)

    def print_contents(self):
        def recur_print(node, level):
            if node.letter:
                print(' '*level + node.letter)
            for child in node.children:
                recur_print(child, level+1)
        recur_print(self.root, 0)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """

        from queue import Queue
        myqueue = Queue()

        for child in self.root.children:
            myqueue.put((child, 0))

        while not myqueue.empty():
            next = myqueue.get()
            node, pos = next
            if node.letter == word[pos] or word[pos] == '.':
                if pos == len(word) - 1:
                    if node.string != '':
                        return True
                else:
                    for child in node.children:
                        myqueue.put((child, pos+1))

        return False


if __name__ == '__main__':
    dictionary = WordDictionary()
    dictionary.addWord("bad")
    dictionary.addWord("dad")
    dictionary.addWord("mad")
    dictionary.print_contents()
    print(dictionary.search("pad"))
    print(dictionary.search("bad"))
    print(dictionary.search(".ad"))
    print(dictionary.search("b.."))
