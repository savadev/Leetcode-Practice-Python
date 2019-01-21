nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0

    previous = nums[0]
    i = 1
    record = 1

    while i < len(nums):
        if nums[i] != previous:

            previous = nums[i]
            nums[record] = nums[i]
            i += 1
            record += 1

        else:
            i += 1
            continue

    nums = nums[:record]

    return len(nums)


removeDuplicates(nums)

class Solution(object):
    def removeDuplicates_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i<len(nums):
            if nums[i-1] == nums[i]:
                del nums[i]
            else:
                i +=1
        return len(nums)