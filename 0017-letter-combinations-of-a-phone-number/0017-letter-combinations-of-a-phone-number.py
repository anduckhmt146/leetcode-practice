class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Subsets = Tree + DFS + Backtrack

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        
        def backtrack(index, path):
            # Base case
            if index == len(digits):
                if path:
                    result.append(''.join(path[:]))
                return

            # Prunning
            for char in phone[digits[index]]:
                # Node
                path.append(char)

                # Neighbor
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result

            