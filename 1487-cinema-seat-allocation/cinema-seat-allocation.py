class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << (s - 1))

        ans = 2 * (n - len(rows))

        for mask in rows.values():
            if mask & 0b0111111110 == 0:
                ans += 2
            elif (
                mask & 0b0000011110 == 0 or   
                mask & 0b0001111000 == 0 or   
                mask & 0b0111100000 == 0      
            ):
                ans += 1

        return ans