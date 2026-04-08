from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Generate squares of sorted array in non-decreasing order.
        Approach: Left & Right Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        idx = n - 1
        
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq > right_sq:
                res[idx] = left_sq
                left += 1
            else:
                res[idx] = right_sq
                right -= 1
            idx -= 1
        return res
