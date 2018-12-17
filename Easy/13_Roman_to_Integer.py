
s = 'IV'
def romanToInt(s):

    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0

    for i in range(len(s)-1):

        if roman[s[i+1]] > roman[s[i]]:
            sum = sum - roman[s[i]]

        else:
            sum = sum + roman[s[i]]

    sum += roman[s[-1]]
    print(sum)
    return sum

romanToInt(s)