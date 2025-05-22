from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store the word at the end node for retrieval

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        # Insert words into the Trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # mark the end of the word

        # DFS to find the longest valid word
        stack = list(root.children.values())
        longest = ""

        while stack:
            node = stack.pop()
            if node.word is not None:  # only consider complete words
                if len(node.word) > len(longest) or \
                   (len(node.word) == len(longest) and node.word < longest):
                    longest = node.word
                for child in node.children.values():
                    stack.append(child)

        return longest
