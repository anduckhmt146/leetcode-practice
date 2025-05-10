class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last = {int(x): i for i, x in enumerate(num_str)}  # last position of each digit

        for i, digit in enumerate(num_str):
            for d in range(9, int(digit), -1):  # check digits larger than current
                if last.get(d, -1) > i:
                    # swap
                    num_str[i], num_str[last[d]] = num_str[last[d]], num_str[i]
                    return int(''.join(num_str))

        return num  # already the maximum
