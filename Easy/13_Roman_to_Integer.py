
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

def romanToInt_2(s):

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0

    for i in range(len(s) - 1):
        print(i)

        print(dict[s[i]])
        if dict[s[i]] < dict[s[i + 1]]:
            value -= dict[s[i]]
        else:
            value += dict[s[i]]
        print(value)

    value += dict[s[-1]]
    print(value)

    return value

romanToInt_2(s)