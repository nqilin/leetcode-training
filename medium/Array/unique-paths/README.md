# [LeetCode 62 - Unique Paths](https://leetcode.com/problems/unique-paths/)
> Difficulty: Medium | Tags: Array, Dynamic Programming, Combinatorics

## 🎯 Problem Description
There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.
Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Examples:
1. Input: m = 3, n = 7 → Output: 28
2. Input: m = 3, n = 2 → Output: 3
   Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
   1. Right → Down → Down
   2. Down → Down → Right
   3. Down → Right → Down
3. Input: m = 7, n = 3 → Output: 28

## 💡 Solution Ideas
1. Core Idea: **Dynamic Programming (DP) with space optimization**
   - State Definition: `dp[i][j]` = number of unique paths to reach cell (i,j)
   - State Transition: `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (paths from top + paths from left)
   - Space Optimization: Use 1D DP array (since we only need previous row's values)
2. Step-by-Step Explanation:
   - Initialize 1D DP array with 1s (first row has only 1 path: all right moves)
   - Iterate from second row to last row:
     - For each column (starting from second), update `dp[j] = dp[j] (top) + dp[j-1] (left)`
   - The last element of DP array is the number of paths to bottom-right corner
3. Edge Cases:
   - m=1 or n=1 (single row/column): only 1 path (all right/down moves)
   - m=2, n=2: 2 paths (Right→Down / Down→Right)

## 📁 Code Files
- [Python Solution](unique_paths.py)
- [C++ Solution](unique_paths.cpp)

## ⚡ Complexity Analysis
- **Time Complexity (TC)**: O(m*n) 
  - Traverse each cell in the grid exactly once (double loop)
  - Optimal time complexity for this problem
- **Space Complexity (SC)**: O(n) 
  - Optimized from 2D DP array (O(m*n)) to 1D DP array (O(n))
  - Can further optimize to O(min(m,n)) by swapping m/n if m < n

## 📌 Problem-Solving Tips
1. Key DP Transition: `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (only two move directions)
2. Space Optimization Logic:
   - 2D DP array stores all previous rows, but we only need the row above current row
   - 1D DP array overwrites itself row by row (dp[j] keeps the value from top row)
3. Alternative Approach (Combinatorics):
   - Total moves needed: (m-1) downs + (n-1) rights = (m+n-2) moves
   - Number of unique paths = C(m+n-2, m-1) = (m+n-2)! / [(m-1)! * (n-1)!]
   - Faster for large m/n (but may have integer overflow without big integer handling)
4. Common Mistake:
   - Initializing DP array with 0s (first row/column should be 1s, as there's only 1 path)
   - Forgetting space optimization (using 2D array is correct but not optimal)

## 📝 Training Log
- Completed Time: 2026-03-09 
- Difficulty Evaluation: ⭐⭐ (1-5 stars)
- Notes: Mastered DP for grid path problems; understood space optimization from 2D to 1D array; learned combinatorics alternative solution
