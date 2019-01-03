class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dict = {1: [1], 2: [1, 1]}
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        dict = {1: [1], 2: [1, 1]}

        start = dict[2]
        pascal = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            nest = []
            for j in range(len(dict[i - 1]) - 1):
                nest.append(dict[i - 1][j] + dict[i - 1][j + 1])
            nest.insert(0, 1)
            nest.append(1)
            dict[i] = nest
            pascal.append(nest)

        return pascal

