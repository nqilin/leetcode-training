from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from a list of strings
    Args:
        strs: List[str] - Input list of strings
    Returns:
        List[List[str]] - Groups of anagrams
    Time Complexity: O(n * k log k) - n = number of strings, k = max length of a string
    Space Complexity: O(n * k) - Store all strings in the hash map
    """
    anagram_map = {}

    for s in strs:
        # Sort the string to get the key
        key = ''.join(sorted(s))

        # Add current string to the corresponding list
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)

    # Return all groups as a list
    return list(anagram_map.values())

# Test
if __name__ == "__main__":
    test = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(test))
