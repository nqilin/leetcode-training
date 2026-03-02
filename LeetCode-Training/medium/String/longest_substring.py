def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters
    Args:
        s: str - Input string
    Returns:
        int - Length of the longest substring without repeating characters
    Time Complexity: O(n) - Traverse the string once (each character visited at most twice)
    Space Complexity: O(min(m, n)) - m is the size of character set (e.g., 128 for ASCII)
    """
    # Hash map to store the last index of each character
    char_index = {}
    # Left pointer of sliding window, max length of valid substring
    left = 0
    max_length = 0
    
    # Right pointer of sliding window (iterate through each character)
    for right, char in enumerate(s):
        # If character exists in map and its index >= left (in current window)
        if char in char_index and char_index[char] >= left:
            # Move left pointer to the right of the repeated character
            left = char_index[char] + 1
        
        # Update the last index of current character
        char_index[char] = right
        # Calculate current window length and update max length
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length

# Test case for verification
if __name__ == "__main__":
    test_cases = ["abcabcbb", "bbbbb", "pwwkew"]
    # Expected outputs: 3, 1, 3
    for case in test_cases:
        print(f"Input: '{case}' → Longest length: {lengthOfLongestSubstring(case)}")
