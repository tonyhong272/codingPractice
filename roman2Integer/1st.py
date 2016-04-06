class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valueDict = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        t=0
        for i in range(len(s)):
            if i<len(s)-1:
                if valueDict[s[i]] < valueDict[s[i+1]]:
                    t -= valueDict[s[i]]
                else:
                    t+= valueDict[s[i]]
            else:
                t += valueDict[s[i]]
        return t

solution = Solution()
s = 'DCCIX'
print(solution.romanToInt(s))