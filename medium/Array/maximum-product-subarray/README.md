# [LeetCode 152 - Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
> Difficulty: Medium | Tags: Array, Dynamic Programming

## 🎯 Problem Description
Given an integer array nums, find a contiguous non-empty subarray that has the **largest product**.

## Examples
- Input: nums = [2,3,-2,4]
- Output: 6
- Explanation: [2,3] has the largest product 6.

- Input: nums = [-2,0,-1]
- Output: 0

## 💡 Solution Ideas
- Use **Dynamic Programming**.
- Track both **current max** and **current min** because negative * negative = positive.
- At each step:
  - new_max = max( nums[i], max*nums[i], min*nums[i] )
  - new_min = min( nums[i], old_max*nums[i], min*nums[i] )
- Update the global result.

## 📁 Code Files
- [Python Solution](max_product.py)
- [C++ Solution](max_product.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1)

## 📝 Training Log
- Completed Time: 2026-03-16
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered DP for product subarray; understand why min must be tracked.
