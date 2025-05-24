class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0  # Count of unmatched '('
        insertions = 0   # Count of insertions needed

        for char in s:
            if char == '(':
                open_needed += 1
            else:  # char == ')'
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1  # Need to insert a '(' before this ')'

        return open_needed + insertions
