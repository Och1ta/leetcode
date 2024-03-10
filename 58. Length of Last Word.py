class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp_str = " ".join(s.split())
        temp_list = temp_str.split(" ")
        return len(temp_list[-1])