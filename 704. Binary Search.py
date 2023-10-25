class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first: int = 0
        last: int = len(nums) - 1
        while first < last:
            mid = (last + first) // 2
            if nums[mid] >= target:
                last = mid
            else:
                first = mid + 1

        if nums[first] != target:
            return -1
        return first
