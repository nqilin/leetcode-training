# [LeetCode 238 - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
> Difficulty: Medium | Tags: Array, Prefix Product

## 🎯 Problem Description
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Constraint: DO NOT USE DIVISION**

## Examples
- Input: nums = [1,2,3,4]
- Output: [24,12,8,6]

## 💡 Solution Ideas
- Use **Prefix & Suffix Product**
- First pass: store left product
- Second pass: multiply by right product
- Result[i] = left product × right product

## 📁 Code Files
- [Python Solution](product_except_self.py)
- [C++ Solution](product_except_self.cpp)

## ⚡ Complexity
- Time: O(n)
- Space: O(1) (output array excluded)

## 📝 Training Log
- Completed Time: 2026-03-18
- Difficulty Evaluation: ⭐⭐⭐
- Notes: Mastered prefix/suffix product pattern for array problems.
