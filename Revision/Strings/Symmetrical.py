def isStringPalindrome(s):
    #Reverse Logic
    str = s[::-1]
    if s == str:
        return True
    else:
        return False

def isStringSymmetrical(s):
    firstHalf=s[0:(len(s)/2)]
    secondHalf = s[(len(s) / 2)-1::-1]
    rev_sechalf=secondHalf[::-1]

    if firstHalf == rev_sechalf:
        return True
    else:
        return False


def isStringSymNPalin(str):
    if isStringSymmetrical(str)==True and isStringPalindrome(str)==False:
        print('The entered string is symmetrical')
        print('The entered string is not palindrome')
    elif isStringSymmetrical(str)==False and isStringPalindrome(str)==True:
        print('The entered string is not symmetrical')
        print('The entered string is palindrome')
    else:
        print('The entered string is symmetrical')
        print('The entered string is palindrome')


val = raw_input('Enter a string\n')
isStringSymNPalin(val)