# LeetCode Easy: Roman to Integer (13)
# https://leetcode.com/problems/roman-to-integer/
# Author: nqilin
# Date: 2026

# Problem: Convert a Roman numeral string to an integer.
# Basic rule: If a numeral is smaller than the next one, subtract it; else add it.

def romanToInt(s: str) -> int:
    """
    Standard solution: Map + single loop + compare left & right
    Time Complexity: O(n)  n = length of string
    Space Complexity: O(1)  fixed map size
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        # If current is less than next → subtract
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]

    return total


def romanToInt_beginner(s: str) -> int:
    """
    Beginner version: More explicit, easier to understand step by step
    Same logic, just written clearer for learning
    """
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0

    for a, b in zip(s, s[1:]):
        if roman[a] < roman[b]:
            res -= roman[a]
        else:
            res += roman[a]

    # Add the last character
    res += roman[s[-1]]
    return res


if __name__ == "__main__":
    # Test cases
    print(romanToInt("III"))      # 3
    print(romanToInt("LVIII"))    # 58
    print(romanToInt("MCMXCIV"))  # 1994
    print(romanToInt("IV"))       # 4
    print(romanToInt("IX"))       # 9
