# LeetCode Easy: Two Sum
**Problem Link**: [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.
- Each input has **exactly one solution**.
- You may not use the **same element** twice.
- The answer can be returned in **any order**.

## Example Inputs & Outputs
### Example 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[7] = 2 + 7 = 9

### Example 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

### Example 3
Input: nums = [3,3], target = 6
Output: [0,1]

## Two Solutions in Python
### Solution 1: Brute Force
- **Idea**: Use double nested `for` loops to check all possible number pairs.
- **Time Complexity**: O(n²) - nested loop traverses the array twice.
- **Space Complexity**: O(1) - no extra data structure is used.
- **Pros**: Simple logic, easy to implement for beginners.
- **Cons**: Low efficiency, not suitable for large arrays.

### Solution 2: Hash Table (Dictionary)
- **Idea**: Use a Python dictionary to map `number value` to its `index`, find the **complement** (target - current number) in O(1) time.
- **Time Complexity**: O(n) - single loop traverses the array once.
- **Space Complexity**: O(n) - extra dictionary to store elements and indices.
- **Pros**: Optimal efficiency, the best solution for this problem.
- **Cons**: Uses a small amount of extra space (trade space for time).

## Tech Stack
- Python 3.x (pure native syntax, no third-party libraries)
- List & Dictionary (Python built-in data structures)
- Enumerate() function for index-value traversal

## Key Learnings
1. **Trade space for time**: A common algorithm optimization strategy (use extra space to reduce time complexity).
2. **Hash Table advantage**: O(1) average time complexity for search/insert operations.
3. **Enumerate() usage**: A Pythonic way to get both index and value when traversing a list.
