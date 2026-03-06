# [LeetCode 53 - Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
> Difficulty: Medium | Tags: Array, Dynamic Programming, Divide and Conquer

## 🎯 Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- A subarray is a contiguous part of an array.

Examples:
1. Input: nums = [-2,1,-3,4,-1,2,1,-5,4] → Output: 6
   Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
2. Input: nums = [1] → Output: 1
3. Input: nums = [5,4,-1,7,8] → Output: 23

## 💡 Solution Ideas
1. Core Idea: **Kadane's Algorithm** (dynamic programming approach)
   - For each position, decide: either start a new subarray with current element, or extend the previous subarray
   - State definition:
     - `current_max`: Maximum sum of subarray ending at current position
     - `global_max`: Maximum sum of all subarrays found so far
2. Step-by-Step Explanation:
   - Initialize `current_max` and `global_max` to the first element (handle edge case of single element)
   - Traverse the array from the second element:
     1. `current_max = max(nums[i], current_max + nums[i])` (key logic)
     2. `global_max = max(global_max, current_max)`
   - Return `global_max`
3. Edge Cases:
   - All negative numbers (e.g., [-3,-1,-2] → return -1)
   - Single element array (e.g., [5] → return 5)
   - All positive numbers (e.g., [1,2,3] → return sum of all elements)

## 📁 Code Files
- [Python Solution](maximum_subarray.py)
- [C++ Solution](maximum_subarray.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(n) 
  - Traverse the array exactly once, each element processed once
  - Optimal time complexity for this problem (cannot solve in less than O(n) time)
- **Space Complexity (SC)**: O(1) 
  - Only use two variables (`current_max`, `global_max`) — optimized version of Kadane's Algorithm
  - Original Kadane's Algorithm uses O(n) space (DP array), this version is space-optimized

## 📌 Problem-Solving Tips
1. Key Logic of Kadane's Algorithm: `current_max = max(num, current_max + num)`
   - If `current_max + num` < num: abandon previous subarray, start new subarray with current num
   - Else: extend previous subarray with current num
2. Alternative Approaches:
   - Divide and Conquer: O(n log n) time (worse than Kadane's, but good for learning divide and conquer)
   - Brute Force: O(n²) time (not recommended, will time out for large arrays)
3. Common Mistake: Initializing `current_max`/`global_max` to 0 (fails for all-negative arrays)
4. Extension: This algorithm is the basis for many subarray sum problems (e.g., maximum subarray sum with at most k elements)

## 📝 Training Log
- Completed Time: 2026-03-06
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered Kadane's Algorithm (core dynamic programming pattern for subarray sum); understood the importance of proper initialization for edge cases
