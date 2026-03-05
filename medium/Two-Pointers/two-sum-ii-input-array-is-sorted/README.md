# [LeetCode 167 - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
> Difficulty: Medium | Tags: Array, Two Pointers, Binary Search

## 🎯 Problem Description
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number.
- Return the indices of the two numbers (1-indexed) as an integer array `answer` of size 2, where `1 <= answer[0] < answer[1] <= numbers.length`.
- The tests are generated such that there is **exactly one solution**.
- You may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

## 💡 Solution Ideas
1. Core Idea: Use **two pointers** (no hash map needed) since the array is sorted (key optimization)
2. Step-by-Step Explanation:
   - Initialize left pointer at the start (0) and right pointer at the end (len(numbers)-1)
   - Calculate the sum of numbers at left/right pointers
   - If sum == target: return 1-indexed indices (left+1, right+1)
   - If sum < target: move left pointer right (to increase sum)
   - If sum > target: move right pointer left (to decrease sum)
   - The array is sorted, so this guarantees finding the solution in O(n) time
3. Edge Cases:
   - Target is sum of first and last elements (e.g., [1,2,3], target=4 → [1,3])
   - Target is sum of adjacent elements (e.g., [2,3,4], target=5 → [1,2])
   - Array with only two elements (e.g., [5,75], target=80 → [1,2])

## 📁 Code Files
- [Python Solution](two_sum_ii.py)
- [C++ Solution](two_sum_ii.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(n) 
  - Traverse the array once with two pointers (each element visited at most once)
  - Better than hash map approach (O(n) space) and binary search approach (O(n log n) time)
- **Space Complexity (SC)**: O(1) 
  - Only use two pointers (constant extra space)
  - Key advantage over the original Two Sum hash map solution (O(n) space)

## 📌 Problem-Solving Tips
1. Key Optimization: Sorted array allows two pointers (no extra space) — this is the optimal solution for this problem
2. 1-Index Note: Remember to add 1 to the indices (common interview mistake)
3. Alternative Approach: Binary search for target - numbers[i] for each i (O(n log n) time, O(1) space)
4. Comparison with Original Two Sum:
   - Original Two Sum (unsorted): hash map is optimal (O(n) time/space)
   - This problem (sorted): two pointers is optimal (O(n) time, O(1) space)
5. Common Mistake: Forgetting the array is sorted and using hash map (works but uses extra space)

## 📝 Training Log
- Completed Time: 2026-03-05
- Difficulty Evaluation: ⭐⭐ (1-5 stars)
- Notes: Mastered two pointers for sorted array sum problems; understood the trade-off between hash map and two pointers based on array order
