class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
            temp = []
            for n in nums1:
                if n in nums2:
                    temp.append(n)
            return list(set(temp))