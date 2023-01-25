def isPalindrome(s):
    str = s[::-1]
    if s==str:
        print("Palindrome")
    else:
        print("Not a Palindrome")


isPalindrome("MAMA")