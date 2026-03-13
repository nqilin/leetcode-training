def countSubstrings(s: str) -> int:
    """
    Count the number of palindromic substrings in a string.
    Approach: Expand Around Center
    Time: O(n²)
    Space: O(1)
    """
    n = len(s)
    count = 0

    def expand(l, r):
        nonlocal count
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    for i in range(n):
        expand(i, i)    # odd
        expand(i, i+1) # even

    return count

if __name__ == "__main__":
    print(countSubstrings("abc"))  # 3
    print(countSubstrings("aaa"))  # 6
