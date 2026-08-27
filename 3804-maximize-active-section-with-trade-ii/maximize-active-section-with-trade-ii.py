from dataclasses import dataclass
import itertools

@dataclass
class Group:
    start: int
    length: int

class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)

        if self.n == 0:
            self.st = []
            return

        k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(k)]
        self.st[0] = nums[:]

        for i in range(1, k):
            size = 1 << i
            half = size >> 1
            for j in range(self.n - size + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j],
                    self.st[i - 1][j + half]
                )

    def query(self, l, r):
        if l > r:
            return 0

        k = (r - l + 1).bit_length() - 1
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )

class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        ones = s.count('1')

        zeroGroups = []
        zeroGroupIndex = []

        for i in range(len(s)):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    zeroGroups[-1].length += 1
                else:
                    zeroGroups.append(Group(i, 1))

            zeroGroupIndex.append(len(zeroGroups) - 1)

        if not zeroGroups:
            return [ones] * len(queries)

        merge = []

        for i in range(len(zeroGroups) - 1):
            merge.append(
                zeroGroups[i].length +
                zeroGroups[i + 1].length
            )

        st = SparseTable(merge)

        ans = []

        for l, r in queries:
            left_id = zeroGroupIndex[l]
            right_id = zeroGroupIndex[r]

            left = -1
            right = -1

            if left_id != -1:
                left = (
                    zeroGroups[left_id].length -
                    (l - zeroGroups[left_id].start)
                )

            if right_id != -1:
                right = (
                    r -
                    zeroGroups[right_id].start +
                    1
                )

            start = left_id + 1
            end = right_id if s[r] == '1' else right_id - 1

            best = ones

            if (
                s[l] == '0'
                and s[r] == '0'
                and left_id + 1 == right_id
            ):
                best = max(best, ones + left + right)

            elif start <= end:
                best = max(
                    best,
                    ones + st.query(start, end - 1)
                )

            if (
                s[l] == '0'
                and left_id + 1 <= (
                    right_id if s[r] == '1'
                    else right_id - 1
                )
            ):
                best = max(
                    best,
                    ones + left +
                    zeroGroups[left_id + 1].length
                )

            if (
                s[r] == '0'
                and left_id < right_id - 1
            ):
                best = max(
                    best,
                    ones + right +
                    zeroGroups[right_id - 1].length
                )

            ans.append(best)

        return ans