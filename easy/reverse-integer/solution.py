# LeetCode Easy: Reverse Integer (7)
# https://leetcode.com/problems/reverse-integer/
# Author: nqilin
# Date: 2026

def reverse(x: int) -> int:
    """
    Solution 1: String reversal (beginner-friendly, easiest to understand)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Convert to string for easy reversal
    s = str(abs(x))
    reversed_s = s[::-1]  # Reverse string (Python classic)
    
    # Convert back to integer
    reversed_num = int(reversed_s)
    
    # Add negative sign if original x is negative
    if x < 0:
        reversed_num = -reversed_num
    
    # Check 32-bit integer range (problem requirement)
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num


def reverse_math(x: int) -> int:
    """
    Solution 2: Pure math (no string, more professional)
    Time Complexity: O(log x)
    Space Complexity: O(1)
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0

    while x > 0:
        last_digit = x % 10
        reversed_num = reversed_num * 10 + last_digit
        x = x // 10

    reversed_num *= sign

    # Check overflow
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0

    return reversed_num


if __name__ == "__main__":
    print(reverse(123))        # 321
    print(reverse(-123))       # -321
    print(reverse(120))        # 21
    print(reverse(0))          # 0
