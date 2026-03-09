#include <vector>
using namespace std;

/**
 * Calculate the number of unique paths from top-left to bottom-right in a m x n grid
 * - Can only move either down or right at any point in time
 * @param m: int - Number of rows in the grid
 * @param n: int - Number of columns in the grid
 * @return: int - Number of unique paths
 * Time Complexity: O(m*n) - Traverse the entire grid once
 * Space Complexity: O(n) - Optimized space (use 1D DP array instead of 2D)
 */
int uniquePaths(int m, int n) {
    // Optimized DP: 1D array (since we only need previous row's values)
    vector<int> dp(n, 1); // First row has only 1 path (all right moves)
    
    // Iterate from second row to last row
    for (int i = 1; i < m; i++) {
        // Iterate from second column to last column
        for (int j = 1; j < n; j++) {
            // Current path count = path from top (dp[j]) + path from left (dp[j-1])
            dp[j] += dp[j-1];
        }
    }
    
    // The bottom-right cell has the total number of unique paths
    return dp[n-1];
}

// Test case for verification
#include <iostream>
int main() {
    // Example 1: m=3, n=7 → Output: 28
    cout << "Unique paths (3x7): " << uniquePaths(3, 7) << endl;
    // Example 2: m=3, n=2 → Output: 3
    cout << "Unique paths (3x2): " << uniquePaths(3, 2) << endl;
    return 0;
}
