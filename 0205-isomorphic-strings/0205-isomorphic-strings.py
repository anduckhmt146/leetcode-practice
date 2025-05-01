class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapStoT = {}
        hashMapTtoS = {}
        for i in range(0, len(s)):
            if s[i] not in hashMapStoT:
                hashMapStoT[s[i]] = t[i]

            if t[i] not in hashMapTtoS:
                hashMapTtoS[t[i]] = s[i]

            if hashMapTtoS[t[i]] != s[i]:
                return False

            if hashMapStoT[s[i]] != t[i]:
                return False
        
        return True
        