from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s.
    Approach: Sliding Window + Frequency Count
    Time: O(n)
    Space: O(1)
    """
    len_s = len(s)
    len_p = len(p)
    res = []

    if len_p > len_s:
        return res

    count_s = [0] * 26
    count_p = [0] * 26

    # Initialize first window
    for i in range(len_p):
        count_p[ord(p[i]) - ord('a')] += 1
        count_s[ord(s[i]) - ord('a')] += 1

    if count_s == count_p:
        res.append(0)

    # Slide window
    for i in range(len_p, len_s):
        # Remove left
        count_s[ord(s[i - len_p]) - ord('a')] -= 1
        # Add right
        count_s[ord(s[i]) - ord('a')] += 1

        if count_s == count_p:
            res.append(i - len_p + 1)

    return res

if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))  # [0,6]
