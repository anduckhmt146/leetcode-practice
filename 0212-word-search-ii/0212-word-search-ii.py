from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie from the words list
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            board[r][c] = '#'  # Mark visited

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:  # Up, Down, Left, Right
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            board[r][c] = char  # Restore after DFS

            # Optional optimization: prune the Trie
            if not next_node.children:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
