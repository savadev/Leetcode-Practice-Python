s = "Hell Woeld"

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s_revised = s[::-1]
    if ' ' in s:
        last_word = s_revised[0:s_revised.rfind(' ', 1)][::-1]
        return len(last_word)
    else:
        print(0)
        return 0

def lengthOfLastWord_2(s):
    last = s.strip()
    if len(last) == 0:
        return len(last)
    else:
        return len(last.split(' ')[-1])

lengthOfLastWord_2(s)