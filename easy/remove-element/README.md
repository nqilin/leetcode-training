# Remove Element (LeetCode 27)
**Difficulty**: Easy
**Link**: [https://leetcode.com/problems/remove-element/](https://leetcode.com/problems/remove-element/)

## Problem Statement
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.
Return the new length of the array after removal.

**Important**:
- Do not allocate extra array space (O(1) extra space only).
- The order of elements may be changed.
- It does not matter what you leave beyond the returned length.

## Examples
- Input: nums = [3,2,2,3], val = 3
  Output: 2, nums = [2,2,...]

- Input: nums = [0,1,2,2,3,0,4,2], val = 2
  Output: 5, nums = [0,1,3,0,4,...]

## Solution: Two Pointers 
1. Use a **slow pointer** to record the position of valid elements.
2. Use a **fast pointer** to traverse the whole array.
3. When `nums[fast] != val`, copy it to `nums[slow]` and move slow forward.
4. The final value of `slow` is the new length.

## Complexity
- **Time Complexity**: O(n) — one pass through the array.
- **Space Complexity**: O(1) — no extra array, only two pointers.

## Key Points
- In-place operation (no new list)
- Two pointers technique (fundamental for array problems)
