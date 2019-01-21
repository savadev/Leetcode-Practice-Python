
s = "A man, a plan, a canal: Panama"
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s_new = ''.join(e for e in s if e.isalnum()).lower()
    print(s_new)

    return s_new == s_new[::-1]

isPalindrome(s)