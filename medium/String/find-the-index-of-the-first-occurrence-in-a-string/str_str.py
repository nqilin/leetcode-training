def strStr(haystack: str, needle: str) -> int:
    """
    Find the first occurrence of needle in haystack (return starting index)
    Return -1 if needle is not part of haystack
    Provide both brute-force and KMP solutions
    Args:
        haystack: str - Source string
        needle: str - Pattern string to find
    Returns:
        int - Starting index of first occurrence, or -1
    Brute-force Time: O(m*n) (m=len(haystack), n=len(needle))
    KMP Time: O(m+n) (linear time, optimal for string matching)
    Space (KMP): O(n) (for prefix table)
    """
    # --------------------------
    # Solution 1: Brute-force (simple, easy to understand)
    # --------------------------
    # m, n = len(haystack), len(needle)
    # # Edge case: needle is empty (per problem definition)
    # if n == 0:
    #     return 0
    # # Iterate through haystack (stop at m-n to avoid out of bounds)
    # for i in range(m - n + 1):
    #     # Check if substring matches needle
    #     if haystack[i:i+n] == needle:
    #         return i
    # # Needle not found
    # return -1

    # --------------------------
    # Solution 2: KMP Algorithm (optimal, linear time)
    # --------------------------
    def build_prefix_table(pattern):
        """Build prefix table (longest prefix suffix) for KMP"""
        n = len(pattern)
        prefix = [0] * n
        # j: length of the previous longest prefix suffix
        j = 0
        for i in range(1, n):
            # Backtrack j until pattern[i] == pattern[j] or j == 0
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix[j-1]
            # If match, increment j and set prefix[i]
            if pattern[i] == pattern[j]:
                j += 1
                prefix[i] = j
        return prefix
    
    m, n = len(haystack), len(needle)
    # Edge cases
    if n == 0:
        return 0
    if m < n:
        return -1
    
    # Build prefix table for needle
    prefix = build_prefix_table(needle)
    j = 0  # Pointer for needle
    
    for i in range(m):
        # Backtrack j using prefix table if mismatch
        while j > 0 and haystack[i] != needle[j]:
            j = prefix[j-1]
        # If match, increment j
        if haystack[i] == needle[j]:
            j += 1
        # If j reaches len(needle), found full match
        if j == n:
            return i - n + 1
    
    # Needle not found
    return -1

# Test case for verification
if __name__ == "__main__":
    test_cases = [
        ("sadbutsad", "sad"),   # Expected: 0
        ("leetcode", "leeto"),  # Expected: -1
        ("mississippi", "issip")# Expected: 4
    ]
    for haystack, needle in test_cases:
        print(f"haystack='{haystack}', needle='{needle}' → Index: {strStr(haystack, needle)}")
