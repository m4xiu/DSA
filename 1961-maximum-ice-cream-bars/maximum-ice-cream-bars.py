class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, x in enumerate(costs):
            if coins < x:
                return i
            coins -= x
        return len(costs)