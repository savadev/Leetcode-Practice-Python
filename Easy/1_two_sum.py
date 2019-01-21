
nums = [3, 3]
target = 6


hashed = {}


def two_sum(nums, target):
    for i in range(len(nums)):
        if target-nums[i] in hashed:
            print([hashed[target-nums[i]], i])
            return [hashed[target-nums[i]], i]

        hashed[nums[i]] = i





def twoSum_2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    j = None
    for i in range(len(nums)):


        num = target - nums[i]

        if num in nums[i + 1:]:
            j = nums[i+1:].index(num)
            print(j)


            print([i,j+i+1])
            return [i, j+i]

twoSum_2(nums, target)
