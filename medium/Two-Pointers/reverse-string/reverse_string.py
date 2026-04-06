from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse input character array in-place.
        Approach: Left & Right Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Left pointer starts at head, right pointer at tail
        left = 0
        right = len(s) - 1

        # Swap characters until two pointers meet
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
