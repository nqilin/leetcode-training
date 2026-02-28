from typing import List

def maxArea(height: List[int]) -> int:
    """
    Calculate the maximum area of water that can be contained by two lines
    Args:
        height: List[int] - Array of non-negative integers representing height of lines
    Returns:
        int - Maximum area of water
    Time Complexity: O(n) - Traverse the array once
    Space Complexity: O(1) - Constant extra space
    """
    # Initialize two pointers and max area
    left = 0
    right = len(height) - 1
    max_area = 0
    
    # Two pointers traverse towards each other
    while left < right:
        # Calculate current area: min height * width
        current_width = right - left
        current_height = min(height[left], height[right])
        current_area = current_height * current_width
        
        # Update max area if current area is larger
        if current_area > max_area:
            max_area = current_area
        
        # Move the pointer with smaller height (key logic)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test case for verification
if __name__ == "__main__":
    test_height = [1,8,6,2,5,4,8,3,7]
    # Expected output: 49
    print(f"Max area: {maxArea(test_height)}")
