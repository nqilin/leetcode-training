# [LeetCode 12 - Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
> Difficulty: Medium | Tags: String, Hash Table, Math

## 🎯 Problem Description
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written largest to smallest from left to right. However, there are six exceptions:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral (1 ≤ num ≤ 3999).

Examples:
1. Input: num = 3 → Output: "III"
2. Input: num = 58 → Output: "LVIII" (L = 50, V = 5, III = 3)
3. Input: num = 1994 → Output: "MCMXCIV" (M = 1000, CM = 900, XC = 90, IV = 4)

## 💡 Solution Ideas
1. Core Idea: **Greedy Algorithm + Predefined Value-Symbol Pairs**
   - Use a list of value-symbol pairs sorted in descending order (include special cases like 4,9,40...)
   - For each pair, append the symbol to the result as many times as possible (subtract the value each time)
   - Early exit when num becomes 0
2. Step-by-Step Explanation:
   - Define all possible value-symbol pairs (13 pairs total, including 6 special cases)
   - Iterate through the pairs from largest to smallest:
     - While num >= current value: append symbol to result, subtract value from num
   - Return the concatenated result string
3. Edge Cases:
   - num = 1 → "I", num = 4 → "IV", num = 9 → "IX"
   - num = 3999 → "MMMCMXCIX" (max value)
   - num = 1000 → "M"

## 📁 Code Files
- [Python Solution](integer_to_roman.py)
- [C++ Solution](integer_to_roman.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(1) 
  - Fixed number of iterations (max 13 steps, one for each value-symbol pair)
  - No dependence on input size (num is bounded 1-3999)
- **Space Complexity (SC)**: O(1) 
  - Fixed size of value-symbol pairs (13 pairs)
  - Result string size is bounded (max 15 characters for 3999)

## 📌 Problem-Solving Tips
1. Key Trick: Include special cases (4,9,40,90,400,900) in the value-symbol list to avoid complex logic
   - Without special cases: need to handle subtraction rules (more code, higher error rate)
2. Greedy Choice: Always use the largest possible symbol first (optimal for this problem)
3. Alternative Approach:
   - Break num into thousands, hundreds, tens, units (e.g., 1994 = 1000 + 900 + 90 + 4)
   - Map each digit to corresponding roman symbols (works but more code)
4. Common Mistake:
   - Forgetting to include special cases (leads to incorrect symbols like "IIII" instead of "IV")
   - Not sorting pairs in descending order (greedy algorithm fails)

## 📝 Training Log
- Completed Time: 2026-03-10
- Difficulty Evaluation: ⭐⭐ (1-5 stars)
- Notes: Mastered greedy algorithm for string conversion problems; understood the importance of predefined special cases to simplify logic
