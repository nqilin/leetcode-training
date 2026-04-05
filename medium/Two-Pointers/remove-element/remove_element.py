from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove target value in-place and return new length.
        Approach: Slow & Fast Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Slow pointer: record position of valid elements
        slow = 0
        # Fast pointer: traverse every element in array
        for fast in range(len(nums)):
            # Keep element if it is not the target value
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        # Slow equals the count of remaining elements
        return slow
