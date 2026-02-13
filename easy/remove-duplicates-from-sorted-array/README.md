# Remove Duplicates from Sorted Array (LeetCode 26)
**Difficulty**: Easy
**Link**: [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem Statement
Given a **sorted** array `nums`, remove duplicates **in-place** such that each element appears only once.
Return the new length of the array.

## Examples
- Input: nums = [1,1,2]
  Output: 2, nums = [1,2,...]
- Input: nums = [0,0,1,1,1,2,2,3,3,4]
  Output: 5, nums = [0,1,2,3,4,...]

## Solution: Two Pointers
1. Use `slow` to place the next unique element.
2. Use `fast` to scan the whole array.
3. If `nums[fast] != nums[fast-1]`, it is a new unique element.
4. Copy to `nums[slow]` and move `slow` forward.
5. Return `slow` as the new length.

## Complexity
- Time: O(n)
- Space: O(1)

## Key Points
- Sorted array: duplicates are adjacent
- In-place modification
- Classic two pointers
