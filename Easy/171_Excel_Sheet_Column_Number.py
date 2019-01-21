class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sum = 0
        for item in s:
            if n >= 0:
                sum = (26 ** (n - 1)) * (ord(item) - 64) + sum
                n -= 1
        return sum

