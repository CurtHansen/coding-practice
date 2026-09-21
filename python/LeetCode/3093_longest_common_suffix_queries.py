class Trie:
    def __init__(self)->None:
        self.root = TrieNode("",0,0,0)
    def add_word(self, word: str, source_pos: int)->None:
        source_length = len(word)
        self.root.process_letter(word,0,source_pos,source_length)
    def search_query(self, query:str)->int:
        search_result = self.root.search(query,0)
        return search_result if search_result is not None else self.root.chosen_source_pos
    def print(self)->None:
        self.root.print()

class TrieNode:
    def __init__(self, letter: str, level: int, source_pos: int|None=None, source_length: int|None=None)->None:
        self.letter = letter
        self.level = level
        self.chosen_source_pos = source_pos
        self.chosen_source_length = source_length
        self.children = dict()
    def process_letter(self, word:str, letter_pos:int, source_pos: int, source_length: int)->None:
        letter = word[letter_pos]
        if letter not in self.children:
            new_node = TrieNode(letter,self.level+1,source_pos,source_length)
            self.children[letter]= new_node
        child = self.children[letter]
        if source_length <= child.chosen_source_length:
            child.chosen_source_pos,child.chosen_source_length = source_pos,source_length
        if letter_pos<len(word)-1:
            child.process_letter(word,letter_pos+1,source_pos,source_length)
    def search(self, query: str, letter_pos:int)->int|None:
        print(f"searching {query=!r} and {letter_pos=!r} in {repr(self)}")
        if letter_pos>=len(query): return None
        query_letter = query[letter_pos]
        print(f"{query_letter=!r}")
        if query_letter not in self.children: return None
        child = self.children[query_letter]
        print(f"for {query_letter=!r}, child is {repr(child)}")
        forward_result = child.search(query,letter_pos+1)
        print(f"{forward_result=!r}")
        return forward_result if forward_result is not None else child.chosen_source_pos
    def __repr__(self)->str:
        return f"TrieNode(letter={self.letter!r},level={self.level!r},source_pos={self.chosen_source_pos!r},source_length={self.chosen_source_length!r})"
    def print(self)->None:
        print(2*self.level*' '+repr(self))
        for c in self.children.values(): c.print()

class Solution:
    def stringIndices(self, dictionary: list[str], queries: list[str]) -> list[int]:
        trie = Trie()
        reversed_dictionary = sorted([(i,x[::-1]) for i,x in enumerate(dictionary)],reverse=True)
        shortest_length = 10**5
        for i,w in reversed_dictionary:
            trie.add_word(w,i)
            if len(w)<=shortest_length:
                shortest_length=len(w)
                trie.root.chosen_source_pos=i
        trie.print()

        n = len(queries)
        results = n*[-1]
        for i,q in enumerate(queries):
            results[i] = trie.search_query(q[::-1])
            print("\n")
        return results


if __name__ == '__main__':
    sol = Solution()
    dictionary = ["abcdefgh", "poiuygh", "ghghgh"]
    queries = ["acbfgh"]
    print(sol.stringIndices(dictionary,queries))