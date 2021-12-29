from typing import *
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    # Palindrome check
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

print(isPalindrome("090"))