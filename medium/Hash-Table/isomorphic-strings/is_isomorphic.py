class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings are isomorphic.
        Approach: Two hash maps for bidirectional mapping
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        map_s_t = {}
        map_t_s = {}

        for c1, c2 in zip(s, t):
            # Check mapping from s to t
            if c1 in map_s_t and map_s_t[c1] != c2:
                return False
            # Check mapping from t to s
            if c2 in map_t_s and map_t_s[c2] != c1:
                return False

            map_s_t[c1] = c2
            map_t_s[c2] = c1

        return True
