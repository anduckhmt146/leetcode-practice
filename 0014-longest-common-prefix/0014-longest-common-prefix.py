class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min(len(word) for word in strs)
        result = ""
        
        for i in range(0, minLen):
            currChar = strs[0][i]
            if all(word[i] == currChar for word in strs):
                result += currChar
            else:
                break
                
        return result
        