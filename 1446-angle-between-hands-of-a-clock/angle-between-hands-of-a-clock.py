class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour % 12) * 30 + minutes * 0.5
        m = minutes * 6
        d = abs(h - m)
        return min(d, 360 - d)