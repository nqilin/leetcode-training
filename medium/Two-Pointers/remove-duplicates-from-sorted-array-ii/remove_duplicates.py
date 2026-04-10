from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Keep at most two duplicates of each element in-place.
        Approach: Slow & Fast Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) <= 2:
            return len(nums)
        
        # slow pointer points to the position to be filled
        slow = 2
        for fast in range(2, len(nums)):
            # keep element if it is not equal to the one at slow-2
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
