from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find unique intersection elements of two arrays.
        Approach: Hash Set for fast lookup
        Time Complexity: O(m + n)
        Space Complexity: O(m)
        """
        set1 = set(nums1)
        res = []
        
        for num in nums2:
            if num in set1:
                res.append(num)
                set1.remove(num)  # avoid duplicate
        
        return res
