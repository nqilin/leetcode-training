# [LeetCode 15 - 3Sum](https://leetcode.com/problems/3sum/) 
> Difficulty: Medium | Tags: Array, Two Pointers, Sorting

## 🎯 Problem Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
- The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
nums[1] + nums[2] + nums[3] = 0 + 1 + 2 = 3 (not zero, excluded).

## 💡 Solution Ideas
1. Core Idea: Sort the array first, then use "fixed one element + two pointers" to find triplets (reduce from O(n³) to O(n²))
2. Step-by-Step Explanation:
   - Sort the array (O(n log n)) to enable two pointers and duplicate removal
   - Iterate each element as the first number of the triplet (nums[i])
   - For each nums[i], use left (i+1) and right (n-1) pointers to find two numbers that sum to -nums[i]
   - Skip duplicate elements (i/left/right) to avoid duplicate triplets
   - Adjust pointers based on current sum (move left if sum < target, move right if sum > target)
3. Edge Cases:
   - Empty array or array length < 3: return empty list
   - All elements are positive/negative: no triplet sums to zero
   - Multiple duplicate elements (e.g., [0,0,0,0]): return only [[0,0,0]]

## 📁 Code Files
- [Python Solution](3sum.py)
- [C++ Solution](3sum.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(n²) 
  - Sorting the array: O(n log n)
  - Nested loop (fixed i + two pointers): O(n²)
  - Overall dominated by O(n²)
- **Space Complexity (SC)**: O(log n) ~ O(n)
  - Depends on the sorting algorithm (Python's sort uses Timsort: O(n) worst case, O(log n) average)
  - No extra space except result storage (not counted in algorithm space complexity)

## 📌 Problem-Solving Tips
1. Key Optimization: Sorting is critical — it enables two pointers and duplicate skipping (the most challenging part of this problem)
2. Duplicate Handling: 
   - Skip duplicate nums[i] (i > 0 and nums[i] == nums[i-1])
   - Skip duplicate left/right after finding a valid triplet
3. Extension: This pattern can be extended to 4Sum (fix two elements + two pointers, O(n³))
4. Common Mistake: Forgetting to skip duplicates leads to redundant triplets in the result

## 📝 Training Log
- Completed Time: 2026-03-01 
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered the "fixed element + two pointers" pattern for sum problems; need to practice duplicate handling more
