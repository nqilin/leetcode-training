from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the array has duplicate elements.
        Approach: Hash Set
        Time: O(n)
        Space: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))  # True
