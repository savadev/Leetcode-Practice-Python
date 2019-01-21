class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        res = ''

        while n > 0:

            r = n % 26
            n = n // 26
            res = s[r] + res
            if r == 0:
                n -= 1

        return res