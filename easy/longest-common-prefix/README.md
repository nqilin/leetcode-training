# Longest Common Prefix (LeetCode 14)
**Difficulty**: Easy
**Link**: [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)

## Problem Statement
Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Examples
- Input: strs = ["flower","flow","flight"]
  Output: "fl"

- Input: strs = ["dog","racecar","car"]
  Output: ""

## Solution Idea
1. Use the **first string** as the initial prefix.
2. Compare this prefix with every other string:
   - If a string does NOT start with the prefix → **shorten the prefix by 1 character from the end**.
   - Repeat until the prefix matches or becomes empty.
3. Return the final prefix.

## Complexity
- **Time Complexity**: O(n * m)
  n = number of strings, m = length of the shortest string
- **Space Complexity**: O(1)
  Only a few extra variables are used.

## Key Points
- String `startswith()` method
- Gradually shorten the prefix
- Handle empty input edge case
