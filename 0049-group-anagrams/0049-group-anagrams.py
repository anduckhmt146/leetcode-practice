class Solution:
    # O(NlogN)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(N * L)
        result = []
        outHashMap = {}
        for i in range(0, len(strs)):
            hashMap = {}
            for character in strs[i]:
                hashMap[character] = hashMap.get(character, 0) + 1
            
            # Sort hashmap by key
            sorted_hashMap = tuple(sorted(hashMap.items()))
            if sorted_hashMap not in outHashMap:
                outHashMap[sorted_hashMap] = []
            outHashMap[sorted_hashMap].append(strs[i])

        return list(outHashMap.values())
            
            



        