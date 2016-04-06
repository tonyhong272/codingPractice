class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC','DCC','DCCC','CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', "I", 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        T = M[num/1000] + C[num%1000/100] + X[num%100/10] + I[num%10]
        return T

solution = Solution()
num = 112
print(solution.intToRoman(num))
