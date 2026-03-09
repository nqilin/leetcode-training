def uniquePaths(m: int, n: int) -> int:
    """
    Calculate the number of unique paths from top-left to bottom-right in a m x n grid
    - Can only move either down or right at any point in time
    Args:
        m: int - Number of rows in the grid
        n: int - Number of columns in the grid
    Returns:
        int - Number of unique paths
    Time Complexity: O(m*n) - Traverse the entire grid once
    Space Complexity: O(n) - Optimized space (use 1D DP array instead of 2D)
    """
    # Optimized DP: 1D array (since we only need previous row's values)
    dp = [1] * n  # First row has only 1 path (all right moves)
    
    # Iterate from second row to last row
    for i in range(1, m):
        # Iterate from second column to last column
        for j in range(1, n):
            # Current path count = path from top (dp[j]) + path from left (dp[j-1])
            dp[j] = dp[j] + dp[j-1]
    
    # The bottom-right cell has the total number of unique paths
    return dp[-1]

# Test case for verification
if __name__ == "__main__":
    # Example 1: m=3, n=7 → Output: 28
    print(f"Unique paths (3x7): {uniquePaths(3, 7)}")
    # Example 2: m=3, n=2 → Output: 3
    print(f"Unique paths (3x2): {uniquePaths(3, 2)}")
