
nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    while i < len(nums):
        print(i)
        print(nums[i])

        if nums[i] == val:
            del nums[i]

        else:
            i += 1

        print(nums)


    return len(nums)

removeElement(nums, val)