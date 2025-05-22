from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store word at end of root

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build Trie from dictionary
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark end of a root word

        def replace(word):
            node = root
            for char in word:
                if char not in node.children:
                    break
                node = node.children[char]
                if node.word:
                    return node.word
            return word

        return ' '.join(replace(w) for w in sentence.split())
