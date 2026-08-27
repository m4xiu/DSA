class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        ans = 0
        energy = 0

        for actual, minimum in tasks:
            if energy < minimum:
                need = minimum - energy
                ans += need
                energy += need

            energy -= actual

        return ans