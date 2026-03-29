class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if ransomNote can be constructed from magazine characters.
        Approach: Hash Map (frequency counting)
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # Count frequency of each character in magazine
        char_count = {}
        for c in magazine:
            char_count[c] = char_count.get(c, 0) + 1

        # Check if ransomNote can be constructed
        for c in ransomNote:
            if char_count.get(c, 0) == 0:
                return False
            char_count[c] -= 1

        return True
