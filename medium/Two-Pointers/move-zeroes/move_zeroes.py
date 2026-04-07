from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros to the end, keep non-zero order.
        Approach: Slow & Fast Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Slow pointer: store position for non-zero numbers
        slow = 0
        # Fast pointer: traverse whole array
        for fast in range(len(nums)):
            # Pick non-zero elements
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # Fill remaining positions with zero
        for i in range(slow, len(nums)):
            nums[i] = 0
