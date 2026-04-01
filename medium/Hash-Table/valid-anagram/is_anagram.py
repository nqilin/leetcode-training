class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if t is an anagram of s.
        Approach: Hash map for character frequency counting
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for c in s:
            count[c] = count.get(c, 0) + 1

        # Decrement count using t
        for c in t:
            count[c] = count.get(c, 0) - 1
            if count[c] < 0:
                return False

        return True
