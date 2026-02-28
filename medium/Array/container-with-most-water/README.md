# [LeetCode 11] Container With Most Water
> Difficulty: Medium | Tags: Array, Two Pointers

## 🎯 Problem Description
Given an integer array `height` of length `n`, find two lines that together with the x-axis form a container, such that the container contains the most water.
- The container's area = min(height[left], height[right]) × (right - left)
- You may not slant the container.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. The maximum area of water (blue section) the container can contain is 49.

## 💡 Solution Ideas
1. Core Idea: Use two pointers to reduce time complexity from O(n²) (brute force) to O(n)
2. Step-by-Step Explanation:
   - Initialize left pointer at start (0) and right pointer at end (len(height)-1)
   - Calculate current area with the two pointers
   - Update max area if current area is larger
   - Move the pointer with smaller height (moving the taller pointer can't increase the area)
3. Edge Cases:
   - If array length < 2: return 0 (no valid container)
   - If all elements are the same: area = element × (length-1)

## 📁 Code Files
- [Python Solution](container_with_most_water.py)
- [C++ Solution](container_with_most_water.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(n) - Traverse the array only once, each element is visited at most once
- **Space Complexity (SC)**: O(1) - Only use constant extra space (pointers and max area variable)

## 📌 Problem-Solving Tips
1. Optimization: Skip duplicate heights (e.g., if height[left] == height[left-1], move left again) to reduce minor calculations
2. Key Insight: The area is limited by the shorter line, so moving the shorter line is the only way to increase area
3. Extension: This two-pointer pattern is widely used in array problems (e.g., 3Sum, Trapping Rain Water)

## 📝 Training Log
- Completed Time: 2026-02-28 
- Difficulty Evaluation: ⭐⭐ (1-5 stars)
- Notes: Mastered the basic two-pointer technique for array problems; need to practice more similar problems
