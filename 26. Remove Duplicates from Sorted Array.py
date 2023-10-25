class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_list = []

        while len(nums) > len(temp_list):
            for i in nums:
                if i not in temp_list:
                    temp_list.append(i)
                if len(nums) > len(temp_list):
                    temp_list.append('_')

        return temp_list
