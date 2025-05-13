class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Step 1: Count the frequency of each number
        count = Counter(arr)

        # Step 2: Sort the frequencies from smallest to largest
        freq_list = sorted(count.values())  # we only care about the frequencies

        # Step 3: Remove the least frequent elements first, reducing k
        unique_count = len(freq_list)
        for freq in freq_list:
            if k >= freq:
                k -= freq
                unique_count -= 1  # one unique number is fully removed
            else:
                break  # can't remove this whole group, stop here

        return unique_count
       