from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        count = 1  # Start with 1 since we always have at least one occurrence

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                # End of a group
                res.append(chars[i - 1])
                if count > 1:
                    for digit in str(count):
                        res.append(digit)
                count = 1  # Reset count for the next character group

        # Modify input list in-place
        chars[:] = res
        return len(res)
