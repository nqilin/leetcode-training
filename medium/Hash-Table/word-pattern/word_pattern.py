class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Check if s follows the same pattern as the given pattern.
        Approach: Bidirectional hash map mapping
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, word in zip(pattern, words):
            # Check char to word mapping
            if c in char_to_word and char_to_word[c] != word:
                return False
            # Check word to char mapping
            if word in word_to_char and word_to_char[word] != c:
                return False

            char_to_word[c] = word
            word_to_char[word] = c

        return True
