# Reverse Integer (LeetCode 7)
**Difficulty**: Easy
**Link**: [https://leetcode.com/problems/reverse-integer/](https://leetcode.com/problems/reverse-integer/)

## Problem Statement
Given a signed 32-bit integer `x`, return `x` with its digits reversed.
If reversing `x` causes the value to go outside the signed 32-bit integer range, return `0`.

## Examples
- Input: 123 → Output: 321
- Input: -123 → Output: -321
- Input: 120 → Output: 21
- Input: 0 → Output: 0

## Constraints
- -2³¹ ≤ x ≤ 2³¹ − 1

## Two Solutions
### Solution 1: String Reversal (Beginner-Friendly)
1. Convert absolute value of x to string.
2. Reverse the string using slicing `[::-1]`.
3. Convert back to integer and restore negative sign.
4. Check 32-bit integer range.

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### Solution 2: Pure Math (Optimal)
1. Extract last digit using `% 10`.
2. Build reversed number using `* 10 + last_digit`.
3. Remove last digit from x using `// 10`.
4. Restore sign and check overflow.

**Time Complexity**: O(log x)
**Space Complexity**: O(1)

## Key Points
- String reverse `s[::-1]`
- Handling negative numbers
- 32-bit integer overflow check
