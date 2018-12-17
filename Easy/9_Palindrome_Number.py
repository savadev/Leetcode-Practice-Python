class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            x_p = str(x)[::-1]
            x_p = int(x_p)

        else:
            return False

        return x == x_p
    