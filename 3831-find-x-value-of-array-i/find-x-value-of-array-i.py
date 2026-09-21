class Solution:
  def resultArray(self, nums: list[int], k: int) -> list[int]:
    ans = [0] * k
    dp = [0] * k

    for num in nums:
      newDp = [0] * k
      numMod = num % k
      newDp[numMod] = 1
      for i in range(k):
        newMod = (i * numMod) % k
        newDp[newMod] += dp[i]
      for i in range(k):
        ans[i] += newDp[i]
      dp = newDp

    return ans
     