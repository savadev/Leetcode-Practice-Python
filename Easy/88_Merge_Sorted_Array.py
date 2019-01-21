nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3



def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1
    k = m+n-1

    while j >= 0 and i >= 0:

        print(i)
        print(j)
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        nums1[:j+1] = nums2[:j+1]
        print(nums1)

    return nums1

def merge_2(nums1, m, nums2, n):
#    nums1 = nums1[:m]
#    nums1.extend(nums2)
    nums1[m:m + n] = nums2
    nums1.sort()
    print(nums1)


merge_2(nums1, m, nums2, n)