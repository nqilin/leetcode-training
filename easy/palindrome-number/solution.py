# LeetCode Easy: Palindrome Number (9)
# https://leetcode.com/problems/palindrome-number/
# Author: nqlin
# Date: 2026

# Problem:
# Given an integer x, return true if x is a palindrome, and false otherwise.
# A palindrome reads the same forward and backward.

def isPalindrome_string(x: int) -> bool:
    """
    Solution 1: Convert to string and reverse (simplest for beginners)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Negative numbers are NOT palindromes
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]  # reverse string and compare


def isPalindrome_math(x: int) -> bool:
    """
    Solution 2: Pure math (no string conversion), more efficient
    Time Complexity: O(log x)
    Space Complexity: O(1)
    """
    # Negative numbers or numbers ending with 0 (and not 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_num = 0
    original = x

    # Reverse half of the number
    while x > reversed_num:
        last_digit = x % 10
        reversed_num = reversed_num * 10 + last_digit
        x = x // 10

    # For even length: x == reversed_num
    # For odd length: x == reversed_num // 10
    return x == reversed_num or x == reversed_num // 10


if __name__ == "__main__":
    # Test cases
    print(isPalindrome_string(121))       # True
    print(isPalindrome_string(-121))      # False
    print(isPalindrome_string(10))        # False
    print(isPalindrome_string(0))         # True

    print(isPalindrome_math(121))         # True
    print(isPalindrome_math(1221))        # True
    print(isPalindrome_math(123))         # False
