nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    max_nums = nums[0]
    before_item_max = nums[0]

    for num in nums[1:]:
        before_item_max = max(before_item_max+num,num)

        max_nums = max(max_nums, before_item_max)

    print(max_nums)
    return max_nums

maxSubArray(nums)