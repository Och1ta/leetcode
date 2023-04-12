class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        index = -1

        while (first <= last) and (index == -1):
            mid = (first + last) // 2

            if nums[mid] == target:
                index = mid
            else:
                if target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        if index == -1:
            index = ((first + last) // 2) + 1

        return index
