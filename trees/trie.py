class TrieNode:

    def __init__(self):
        self.nodes = {}
        self.is_leaf = False

    def insert_word(self, word):

        current_node = self
        for char in word:
            if char not in current_node.nodes[char]:
                current_node.nodes[char] = TrieNode()
                current_node = current_node.nodes[char]
            curr.is_leaf = True

    def find(self, word):
        pass
