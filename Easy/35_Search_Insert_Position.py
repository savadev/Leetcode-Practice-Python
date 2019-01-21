nums = [1,3,5,6]
target = 7

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    i = 0

    if target in nums:
        return nums.index(target)

    else:

        while i < len(nums):
            if target < nums[i]:
                print(i)
                return i
            i += 1

        print(i)
        return i


class Solution(object):
    def searchInsert_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)


searchInsert(nums, target)