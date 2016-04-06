class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        preStr = ''
        if not strs:
            return preStr
        for i, char in enumerate(strs[0]):
            for string in (strs):
                if len(string) -1 < i or char != string[i]:
                    return preStr
            preStr += char
        return preStr

solution = Solution()
strs = ['ba','ba']
print (solution.longestCommonPrefix(strs))