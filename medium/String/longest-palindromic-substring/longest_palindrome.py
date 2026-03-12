def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    Approach: Expand Around Center (two pointers)
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not s:
        return ""

    n = len(s)
    start = 0
    end = 0

    def expand(left: int, right: int) -> int:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand(i, i)    # odd length
        len2 = expand(i, i+1) # even length
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]

if __name__ == "__main__":
    print(longestPalindrome("babad"))  # "bab" or "aba"
    print(longestPalindrome("cbbd"))   # "bb"
