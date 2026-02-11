# LeetCode Easy: Longest Common Prefix (14)
# https://leetcode.com/problems/longest-common-prefix/
# Author: nqilin
# Date: 2026

def longestCommonPrefix(strs):
    """
    Find the longest common prefix string among an array of strings.
    Time Complexity: O(n * m)
    Space Complexity: O(1)
    """
    if not strs:
        return ""

    # Take the first string as prefix
    prefix = strs[0]

    # Compare with every other string
    for s in strs[1:]:
        # While current string does NOT start with prefix
        while not s.startswith(prefix):
            # Shorten the prefix by 1 character
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"
    print(longestCommonPrefix(["dog","racecar","car"]))     # ""
    print(longestCommonPrefix(["apple", "app", "application"]))  # "app"
