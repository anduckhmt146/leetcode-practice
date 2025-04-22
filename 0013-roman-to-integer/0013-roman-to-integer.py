class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        val = 0
        for i in range(0, len(s)):
            if i < len(s) - 1 and hashMap[s[i]] < hashMap[s[i + 1]]:
                val -= hashMap[s[i]]
            else:
                val += hashMap[s[i]]

        return val
        