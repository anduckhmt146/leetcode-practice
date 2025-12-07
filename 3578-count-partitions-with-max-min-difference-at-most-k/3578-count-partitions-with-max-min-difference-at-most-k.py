# class Solution:
#     def countPartitions(self, nums, k):
#         n = len(nums)

#         def backtrack(start):
#             # If we used the entire array, 1 valid partition
#             if start == n:
#                 return 1

#             res = 0
#             cur_min = cur_max = nums[start]

#             for end in range(start, n):
#                 cur_min = min(cur_min, nums[end])
#                 cur_max = max(cur_max, nums[end])

#                 if cur_max - cur_min <= k:
#                     res += backtrack(end + 1)
#                 else:
#                     break   # further expanding only increases diff

#             return res

#         return backtrack(0)


# class Solution:
#     def countPartitions(self, nums, k):
#         n = len(nums)
#         dp = [0] * (n + 1)
#         dp[0] = 1  # empty prefix

#         for i in range(1, n + 1):
#             cur_min = cur_max = nums[i - 1]

#             # expand backwards: j → i-1
#             for j in range(i - 1, -1, -1):
#                 cur_min = min(cur_min, nums[j])
#                 cur_max = max(cur_max, nums[j])

#                 if cur_max - cur_min <= k:
#                     dp[i] += dp[j]
#                 else:
#                     break  # too wide, will only get worse

#         return dp[n]


class Solution:
    def countPartitions(self, nums, k):
        from collections import deque

        n = len(nums)

        # dp[i] = number of ways to partition nums[0:i]
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[0] = 1
        prefix[0] = 1

        maxD = deque()  # monotonic decreasing (store indices)
        minD = deque()  # monotonic increasing (store indices)

        left = 0  # left boundary for valid window

        for right in range(1, n + 1):
            val = nums[right - 1]

            # ---- maintain max deque ----
            while maxD and nums[maxD[-1]] < val:
                maxD.pop()
            maxD.append(right - 1)

            # ---- maintain min deque ----
            while minD and nums[minD[-1]] > val:
                minD.pop()
            minD.append(right - 1)

            # ---- shrink window until valid ----
            while nums[maxD[0]] - nums[minD[0]] > k:
                left += 1
                if maxD[0] < left:
                    maxD.popleft()
                if minD[0] < left:
                    minD.popleft()

            # ---- DP transition using prefix sum ----
            dp[right] = prefix[right - 1] - (prefix[left - 1] if left > 0 else 0)
            prefix[right] = prefix[right - 1] + dp[right]

        return dp[n] % (10**9 + 7)

