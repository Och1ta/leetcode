class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = min([len(s) for s in strs])
        result_s = ''

        for i in range(0, min_len):
            temp_s = strs[0][i]
            for s in strs:
                if temp_s != s[i]:
                    return result_s
            else:
                result_s += temp_s

        return result_s
