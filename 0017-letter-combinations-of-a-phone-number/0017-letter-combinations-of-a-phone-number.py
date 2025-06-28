class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        # Calculate in the backtrack function
        def backtrack(index, path):
            if index == len(digits):
                res.append(path[:])
                return

            keyboardChar = digitMapping[digits[index]]
            for char in keyboardChar:
                # Move the logic to backtrack function too
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return res if digits != "" else []

        