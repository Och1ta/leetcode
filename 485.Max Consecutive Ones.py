class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = n = 0
        for i in nums:
            if i == 1:
                k += 1
            else:
                n: int = max(k,n)
                k: int = 0
        return max(n, k)
