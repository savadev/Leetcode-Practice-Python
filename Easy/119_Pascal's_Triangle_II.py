class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        dict = {0: [1], 1: [1, 1]}

        for i in range(2, rowIndex + 1):
            nest = []
            for j in range(len(dict[i - 1]) - 1):
                nest.append(dict[i - 1][j] + dict[i - 1][j + 1])

            nest.insert(0, 1)
            nest.append(1)
            dict[i] = nest
        return dict[rowIndex]