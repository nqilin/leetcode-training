from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers in a sorted array that add up to a target (1-indexed)
    Args:
        numbers: List[int] - Sorted non-decreasing integer array
        target: int - Target sum
    Returns:
        List[int] - 1-indexed indices of the two numbers (first < second)
    Time Complexity: O(n) - Traverse the array once with two pointers
    Space Complexity: O(1) - Constant extra space (no hash map)
    """
    # Initialize two pointers: left at start, right at end
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-indexed indices
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1
    
    # Problem guarantees exactly one solution, so no need for default return
    return []

# Test case for verification
if __name__ == "__main__":
    test_numbers = [2,7,11,15]
    test_target = 9
    # Expected output: [1,2]
    print(f"Indices: {twoSum(test_numbers, test_target)}")
