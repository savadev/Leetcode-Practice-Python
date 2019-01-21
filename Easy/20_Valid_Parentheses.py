s = '{[()]}'


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    dict = {"}": "{", "]": "[", ")": "("}
    stack = []

    for char in s:
        print(stack)
        if char in dict.values():
            print(char)
            stack.append(char)
            print(stack)
        elif char in dict.keys():
            print(char)
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

isValid(s)