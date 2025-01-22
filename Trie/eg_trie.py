 

class Trie:
    """
    A standard trie storing lowercase, alphabetic words. No compression
    """

    class TrieNode:
        def __init__(self, letter):
            self.letter = letter
            self.is_word = False
            self.children = [None] * 26
            self.num_children = 0


        @staticmethod
        def index(char: str) -> int:
            return ord(char) - 97


        def get_child(self, char: str):
            return self.children[self.index(char)]


        def create_child(self, char: str):
            if self.children[self.index(char)] is None:
                self.children[self.index(char)] = Trie.TrieNode(char)
                self.num_children += 1


        def remove_child(self, char: str):
            if self.children[self.index(char)] is not None:
                self.children[self.index(char)] = None
                self.num_children -= 1



    def __init__(self):
        self.root = self.TrieNode(None)


    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.get_child(char) is None:
                node.create_child(char)
            node = node.get_child(char)
        node.is_word = True


    def find(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.get_child(char) is None:
                return False
            node = node.get_child(char)
        return node.is_word


    def delete(self, word: str) -> None:
        if self.find(word):
            # Traverse to bottom node
            path = [self.root]
            for char in word:
                path.append(path[-1].get_child(char))

            # If deleted word is a prefix
            path[-1].is_word = False
            if path[-1].num_children > 0:
                return

            # Traverse upwards until fork
            idx = len(path) - 1
            while path[idx].num_children < 2 and not path[idx].is_word and idx > 0:
                last_char = path[idx].letter
                idx -= 1
            path[idx].remove_child(last_char)



"========= Testing Trie ========="

def test_trie():
    # t = Trie()
    # t.insert('many')
    # print(t.find('many'))
    # print(t.find('m'))
    # print(t.find('abc'))
    # print(t.find('manyy'))

    one_word = Trie()
    one_word.insert('word')

    disjoint = Trie()
    disjoint.insert('able')
    disjoint.insert('body')
    disjoint.insert('cat')

    many = Trie()
    many.insert('many')
    many.insert('my')
    many.insert('myself')
    many.insert('able')

    one_word.delete('word')

    disjoint.delete('able')
    disjoint.delete('body')
    disjoint.delete('cat')

    print(many.find('myself'))
    print(many.find('my'))
    print(many.find('many'))
    print(many.find('mys'))

    many.delete('my')
    print(many.find('myself'))
    print(many.find('my'))
    print(many.find('many'))
    print(many.find('mys'))


test_trie()