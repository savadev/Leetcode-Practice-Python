class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}
        for index, value in enumerate(numbers, 1):
            if target - value in dict:
                return [dict[target - value], index]
            else:
                dict[value] = index

                