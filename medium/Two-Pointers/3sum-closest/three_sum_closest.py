from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Find three integers whose sum is closest to target.
        Approach: Sort + Two Pointers
        Time Complexity: O(n^2)
        Space Complexity: O(log n)
        """
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # update closest sum
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # exact match, return immediately
                    return target
        return closest
