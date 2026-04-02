# [LeetCode 349 - Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
> Difficulty: Easy | Tags: Array, Hash Table

## 🎯 Problem Description
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique.

## Examples
- Input: nums1 = [1,2,2,1], nums2 = [2,2]
- Output: [2]

## 💡 Solution Ideas
1. Store elements of first array in hash set for O(1) lookup.
2. Traverse second array, collect elements existing in the set.
3. Remove element from set after collecting to ensure uniqueness.

## 📁 Code Files
- [Python Solution](intersection.py)
- [C++ Solution](intersection.cpp)

## ⚡ Complexity Analysis
- Time Complexity: O(m + n)
- Space Complexity: O(m)

## 📌 Key Points
- Hash set deduplication & fast search
- Guarantee unique result elements

## 📝 Training Log
- Completed Time: 2026-04-02
- Difficulty Evaluation: ⭐
- Notes: Practiced hash set for array intersection problem.
