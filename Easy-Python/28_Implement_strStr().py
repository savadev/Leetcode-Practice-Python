
haystack = "hello"
needle = "ll"

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if needle in haystack:
        return haystack.index(needle)

    else:
        return -1

strStr(haystack, needle)