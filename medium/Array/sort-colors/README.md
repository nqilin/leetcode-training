# [LeetCode 75 - Sort Colors](https://leetcode.com/problems/sort-colors/)
> Difficulty: Medium | Tags: Array, Two Pointers, Sorting

## 🎯 Problem Description
Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
- We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.
- You must solve this problem without using the library's sort function.
- Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Examples:
1. Input: nums = [2,0,2,1,1,0] → Output: [0,0,1,1,2,2]
2. Input: nums = [2,0,1] → Output: [0,1,2]
3. Input: nums = [0] → Output: [0]

## 💡 Solution Ideas
1. Core Idea: **Three Pointers (Dutch National Flag Algorithm)** 
   - Partition the array into three regions: 0s (left), 1s (middle), 2s (right)
   - Avoid two-pass counting sort (count 0/1/2 then rewrite array) — use one-pass solution
2. Step-by-Step Explanation:
   - `left`: Right boundary of 0s (all elements before `left` are 0)
   - `current`: Current element to check (traverse the array)
   - `right`: Left boundary of 2s (all elements after `right` are 2)
   - Traverse with `current` until it exceeds `right`:
     1. If `nums[current] == 0`: swap with `nums[left]`, move `left` and `current` forward
     2. If `nums[current] == 1`: move `current` forward (1 is in correct region)
     3. If `nums[current] == 2`: swap with `nums[right]`, move `right` backward (do NOT move `current`!)
3. Edge Cases:
   - All elements are the same (e.g., [0,0,0] or [2,2,2])
   - Array with only two elements (e.g., [1,0] → [0,1])
   - Already sorted array (e.g., [0,1,2] → no changes)

## 📁 Code Files
- [Python Solution](sort_colors.py)
- [C++ Solution](sort_colors.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(n) 
  - One-pass traversal: each element is processed exactly once (swapped at most once)
  - Better than two-pass counting sort (same O(n) time but one-pass is more optimal)
- **Space Complexity (SC)**: O(1) 
  - Only three pointers (constant extra space)
  - In-place sorting (no extra array needed)

## 📌 Problem-Solving Tips
1. Key Rule: Do NOT move `current` when swapping with `right` (swapped element may be 0/2 and needs recheck)
   - Example: If `nums[current] = 2` and `nums[right] = 0`, swapping gives `nums[current] = 0` — need to check this 0 with `left`
2. Alternative Approach (Two-Pass):
   - Count the number of 0s, 1s, 2s (first pass)
   - Rewrite the array with 0s first, then 1s, then 2s (second pass)
   - Simpler but not optimal (two-pass instead of one-pass)
3. Common Mistake: Moving `current` forward after swapping with `right` (leads to unprocessed elements)
4. Extension: This pattern can be extended to sort arrays with more partitions (e.g., 4 colors)

## 📝 Training Log
- Completed Time: 2026-03-07
- Difficulty Evaluation: ⭐⭐⭐ (1-5 stars)
- Notes: Mastered Dutch National Flag Algorithm (three pointers for in-place partitioning); understood the critical rule of not moving current after swapping with right
