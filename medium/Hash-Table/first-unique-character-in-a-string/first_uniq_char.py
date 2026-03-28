class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Find the first non-repeating character in a string and return its index.
        Approach: Hash Map (frequency counting)
        Time Complexity: O(n)
        Space Complexity: O(1) (only 26 lowercase letters)
        """
        # Count frequency of each character
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        # Find the first character with frequency 1
        for idx, c in enumerate(s):
            if freq[c] == 1:
                return idx

        # No unique character exists
        return -1
