strs = ["flower","flow","flight"]


def longestCommonPrefix(strs):
    prefix = ''
    for i in zip(*strs):
        if len(set(i)) == 1:
            prefix = prefix + i[0]
        else:
            break
    print(prefix)
    return prefix


longestCommonPrefix(strs)