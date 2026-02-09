# Roman to Integer (LeetCode 13)
**Difficulty**: Easy  
**Link**: [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)

## Problem Statement
Given a Roman numeral string `s`, convert it to an integer.

## Roman Numeral Rules
- I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
- If a smaller numeral is before a larger one → **subtract** the smaller
- Otherwise → **add** the value

### Examples
- Input: "III" → Output: 3
- Input: "IV" → Output: 4
- Input: "IX" → Output: 9
- Input: "LVIII" → Output: 58
- Input: "MCMXCIV" → Output: 1994

## Solution
### Core Idea
1. Create a **dictionary** to map each Roman character to its integer value.
2. Traverse the string from left to right.
3. If current value < next value → subtract current value.
4. Else → add current value.
5. Return total sum.

### Complexity
- **Time Complexity**: O(n) (single pass through string)
- **Space Complexity**: O(1) (fixed-size dictionary, no extra space)

## Key Edge Cases
- Subtractive combinations: IV, IX, XL, XC, CD, CM
- Single character (I, V, X, etc.)
- Long mixed string (MCMXCIV)

## What You Learn
- Roman numeral conversion logic
- Dictionary mapping (practical use case)
- Left-right comparison in string traversal
- Clean loop + condition algorithm structure
