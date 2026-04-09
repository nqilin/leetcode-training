from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers such that they add up to target.
        The input array is sorted in non-decreasing order.
        Approach: Left & Right Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
