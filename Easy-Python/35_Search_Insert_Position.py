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




searchInsert(nums, target)